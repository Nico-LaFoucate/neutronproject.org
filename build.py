#!/usr/bin/env python3
"""Build the Neutron wiki: Markdown in wiki-src/ -> static pages in wiki/.

    python3 build.py           regenerate wiki/ (and sitemap.xml once INDEXABLE is on)
    python3 build.py --check   exit 1 if the committed output is out of date

Edit wiki-src/, never wiki/: everything under wiki/ is generated and overwritten.

    wiki-src/nav.json        groups, sections, categories and article order
    wiki-src/pages/<section>/<category>/<article>.md
                             front matter (title, status, sub) and a Markdown body;
                             an empty body renders the "being written" note
    wiki-src/template.html   the page shell: head, top bar, footer
    wiki-src/wiki.css        copied to wiki/wiki.css
    wiki-src/wiki.js         copied to wiki/wiki.js with the search index filled in

Each article is served at /wiki/<section>/<category>/<article>/. Old /wiki/#/... links
are sent to the new address by a small script on /wiki/. Empty "being written" articles
are still built, so old links keep working, but they are left out of the sidebar, the
listings, search and the sitemap; so is a category with nothing else in it.

Markdown: paragraphs, "## " and "### " headings, "- " lists, **bold**, *italic*,
`code` and [text](/wiki/...) links. A block that starts with an HTML tag such as
<div class="callout"> is copied through unchanged. Standard library only.
"""
import html
import json
import re
import sys
from pathlib import Path

SITE_URL = "https://neutronproject.org"
# Pre-launch: every wiki page carries noindex and no sitemap is written.
# Launch day: set this to True and rebuild (see robots.txt as well).
INDEXABLE = False

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "wiki-src"
OUT = ROOT / "wiki"
SITEMAP = ROOT / "sitemap.xml"

BADGE = {"fix": "Fixed", "feature": "Feature", "issue": "Known issue", "guide": "Guide", "stub": "Being written"}
STUB = ('<div class="stub-note"><b>This page is being written.</b> The structure is in place; the content '
        'is on its way. If you have notes or hit something relevant here, that feedback shapes what gets '
        'written first.</div>')
HOME_TITLE = "Neutron Wiki"
HOME_SUB = ("How the stack works, what each part does, the fixes behind it, and how to troubleshoot — organized "
            "by the part of the stack you’re looking at. Pick a component, then a category, then the specific thing.")
HOME_DESC = ("The Neutron project wiki: how the stack works, what each part does, the fixes behind it, and how to "
             "troubleshoot — organized by component.")
SEARCH_ICON = ('<svg width="13" height="13" viewBox="0 0 13 13"><circle cx="5.5" cy="5.5" r="4" fill="none" '
               'stroke="#8B97AD" stroke-width="1.3"/><line x1="8.5" y1="8.5" x2="12" y2="12" stroke="#8B97AD" '
               'stroke-width="1.3"/></svg>')


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- Markdown

def inline(s):
    codes = []

    def keep(m):
        codes.append("<code>%s</code>" % html.escape(m.group(1), quote=False))
        return "\x00%d\x00" % (len(codes) - 1)

    s = re.sub(r"`([^`]+)`", keep, s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a class="ln" href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)


BLOCK_TAG = re.compile(r"<(div|p|ul|ol|table|figure|section|nav|h[1-6]|!--)[\s>]")


def markdown(text):
    out, para, items = [], [], []

    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para.clear()
        if items:
            out.append("<ul>\n%s\n</ul>" % "\n".join("<li>%s</li>" % inline(i) for i in items))
            items.clear()

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
        elif not para and not items and BLOCK_TAG.match(s):
            block = []
            while i < len(lines) and lines[i].strip():
                block.append(lines[i])
                i += 1
            out.append("\n".join(block))
            continue
        elif s.startswith("### "):
            flush()
            out.append("<h3>%s</h3>" % inline(s[4:]))
        elif s.startswith("## "):
            flush()
            out.append("<h2>%s</h2>" % inline(s[3:]))
        elif s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
        elif items and line.startswith("  "):
            items[-1] += " " + s
        else:
            if items:
                flush()
            para.append(s)
        i += 1
    flush()
    return "\n".join(out)


def read_article(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)\Z", text, re.S)
    if not m:
        sys.exit("%s: missing front matter" % path)
    meta = {}
    for line in m.group(1).split("\n"):
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    for key in ("title", "status"):
        if not meta.get(key):
            sys.exit("%s: front matter needs '%s'" % (path, key))
    if meta["status"] not in BADGE:
        sys.exit("%s: status must be one of %s" % (path, ", ".join(BADGE)))
    body = m.group(2).strip()
    meta["sub"] = meta.get("sub", "")
    meta["html"] = markdown(body) if body else STUB
    meta["stub"] = not body
    return meta


# ---------------------------------------------------------------- site model

def load():
    nav = json.loads((SRC / "nav.json").read_text(encoding="utf-8"))
    sections = []
    for g in nav["groups"]:
        for s in g["sections"]:
            s["group"] = g
            for c in s["categories"]:
                c["arts"] = []
                for slug in c["articles"]:
                    p = SRC / "pages" / s["slug"] / c["slug"] / (slug + ".md")
                    if not p.exists():
                        sys.exit("nav.json lists %s, which does not exist" % p.relative_to(ROOT))
                    a = read_article(p)
                    a["slug"] = slug
                    c["arts"].append(a)
                c["shown"] = [a for a in c["arts"] if not a["stub"]]
            s["shown"] = [c for c in s["categories"] if c["shown"]]
            sections.append(s)
    listed = {(s["slug"], c["slug"], a["slug"]) for s in sections for c in s["categories"] for a in c["arts"]}
    for p in (SRC / "pages").rglob("*.md"):
        key = p.relative_to(SRC / "pages").with_suffix("").parts
        if key not in listed:
            sys.exit("%s is not listed in nav.json" % p.relative_to(ROOT))
    return nav, sections


def url(*parts):
    return "/wiki/" + "".join(p + "/" for p in parts if p)


# ---------------------------------------------------------------- rendering

def sidebar(nav, sec=None, cat=None, art=None):
    h = ['<div class="search">%s<input id="q" placeholder="Search the wiki…" autocomplete="off" '
         'aria-label="Search the wiki"></div>' % SEARCH_ICON, '<div class="tree" id="tree">']
    for g in nav["groups"]:
        active_in = any(s["slug"] == sec for s in g["sections"])
        is_open = active_in or g["open"]
        h.append('<div class="grp toggle" role="button" tabindex="0" aria-expanded="%s" data-group="%s"%s>'
                 '<span class="chev">%s</span>%s</div>'
                 % ("true" if is_open else "false", esc(g["label"]), " data-active" if active_in else "",
                    "▾" if is_open else "▸", esc(g["label"])))
        h.append('<div class="grp-body"%s>' % ("" if is_open else " hidden"))
        for s in g["sections"]:
            active = s["slug"] == sec
            h.append('<div class="snode%s"><a href="%s">%s<span class="kind">%s</span></a></div>'
                     % (" active" if active else "", url(s["slug"]), esc(s["title"]), esc(s["kind"])))
            if not active:
                continue
            for c in s["shown"]:
                c_active = c["slug"] == cat
                h.append('<div class="cat%s"><a href="%s">%s</a></div>'
                         % (" active" if c_active else "", url(s["slug"], c["slug"]), esc(c["title"])))
                if c_active:
                    links = "".join(
                        '<a%s href="%s"><span class="dot %s"></span>%s</a>'
                        % (' class="active" aria-current="page"' if a["slug"] == art else "",
                           url(s["slug"], c["slug"], a["slug"]), a["status"], esc(a["title"]))
                        for a in c["shown"])
                    h.append('<div class="arts">%s</div>' % links)
        h.append("</div>")
    h.append("</div>")
    return "\n".join(h)


def crumb(parts):
    return '<nav class="crumb">' + " ".join(
        ('<span class="sep">/</span>' if i else "")
        + ('<a href="%s">%s</a>' % (href, esc(t)) if href else "<span>%s</span>" % esc(t))
        for i, (t, href) in enumerate(parts)) + "</nav>"


def page(template, nav, route, title, description, content, head_extra=""):
    sec, cat, art = (list(route) + [None] * 3)[:3]
    path = url(*route)
    return (template
            .replace("{{robots}}", "" if INDEXABLE else '<meta name="robots" content="noindex, nofollow">\n')
            .replace("{{title}}", esc(title))
            .replace("{{description}}", esc(description))
            .replace("{{canonical}}", SITE_URL + path)
            .replace("{{head_extra}}", head_extra)
            .replace("{{sidebar}}", sidebar(nav, sec, cat, art))
            .replace("{{content}}", content))


def redirect_script(routes):
    # Old links looked like /wiki/#/section/category/article. Send them to the static page,
    # or to the nearest page that still exists.
    return ("<script>\n(function(){var h=location.hash;if(h.indexOf('#/')!==0)return;"
            "var p=h.slice(2).split('?')[0];try{p=decodeURIComponent(p);}catch(e){}"
            "var R=%s;var s=p.split('/').filter(Boolean);"
            "while(s.length){if(R.indexOf(s.join('/'))>=0){location.replace('/wiki/'+s.join('/')+'/');return;}s.pop();}"
            "})();\n</script>\n" % json.dumps(routes, separators=(",", ":")))


def build():
    nav, sections = load()
    template = (SRC / "template.html").read_text(encoding="utf-8")
    files, index, routes, sitemap_urls = {}, [], [], ["/", url()]

    def emit(route, title, description, content, head_extra="", in_sitemap=True):
        rel = Path(*route, "index.html") if route else Path("index.html")
        files[rel] = page(template, nav, route, title, description, content, head_extra)
        if in_sitemap and route:
            sitemap_urls.append(url(*route))

    # article, category and section pages
    for s in sections:
        sk = s["slug"]
        routes.append(sk)
        cards = "".join('<a class="card" href="%s"><div class="ct">%s</div><p>%d %s</p></a>'
                        % (url(sk, c["slug"]), esc(c["title"]), len(c["shown"]),
                           "article" if len(c["shown"]) == 1 else "articles") for c in s["shown"])
        emit((sk,), "%s — %s" % (s["title"], HOME_TITLE), s["blurb"],
             crumb([("Wiki", url()), (s["title"], None)])
             + '\n<h1 class="title">%s</h1><p class="subtitle">%s</p><div class="cards">%s</div>'
             % (esc(s["title"]), esc(s["blurb"]), cards))
        for c in s["categories"]:
            ck = c["slug"]
            routes.append("%s/%s" % (sk, ck))
            cards = "".join('<a class="card" href="%s"><div class="ct"><span class="dot %s"></span>%s</div>'
                            '<div class="ck">%s</div>%s</a>'
                            % (url(sk, ck, a["slug"]), a["status"], esc(a["title"]), BADGE[a["status"]],
                               "<p>%s</p>" % esc(a["sub"]) if a["sub"] else "") for a in c["shown"])
            emit((sk, ck), "%s · %s — %s" % (c["title"], s["title"], HOME_TITLE), s["blurb"],
                 crumb([("Wiki", url()), (s["title"], url(sk)), (c["title"], None)])
                 + '\n<h1 class="title">%s</h1><p class="subtitle">%s</p><div class="cards">%s</div>'
                 % (esc(c["title"]), esc(s["title"]), cards), in_sitemap=bool(c["shown"]))
            for a in c["arts"]:
                ak = a["slug"]
                routes.append("%s/%s/%s" % (sk, ck, ak))
                if not a["stub"]:
                    index.append({"t": a["title"], "s": a["sub"], "S": s["title"], "C": c["title"],
                                  "h": url(sk, ck, ak), "st": a["status"]})
                body = (crumb([("Wiki", url()), (s["title"], url(sk)), (c["title"], url(sk, ck)), (a["title"], None)])
                        + '\n<div><span class="badge b-%s">%s</span></div>\n<h1 class="title">%s</h1>\n'
                        % (a["status"], BADGE[a["status"]], esc(a["title"]))
                        + ('<p class="subtitle">%s</p>\n' % esc(a["sub"]) if a["sub"] else "")
                        + a["html"])
                emit((sk, ck, ak), "%s — %s" % (a["title"], HOME_TITLE), a["sub"] or s["blurb"], body,
                     in_sitemap=not a["stub"])

    # wiki home
    home = [crumb([("Wiki", None)]),
            '<h1 class="title">%s</h1><p class="subtitle">%s</p>' % (HOME_TITLE, esc(HOME_SUB))]
    for g in nav["groups"]:
        home.append('<h2>%s</h2><div class="cards">%s</div>' % (esc(g["label"]), "".join(
            '<a class="card" href="%s"><div class="ct">%s</div><div class="ck">%s</div><p>%s</p></a>'
            % (url(s["slug"]), esc(s["title"]), esc(s["kind"]), esc(s["blurb"])) for s in g["sections"])))
    emit((), HOME_TITLE, HOME_DESC, "\n".join(home), head_extra=redirect_script(routes))

    files[Path("wiki.css")] = (SRC / "wiki.css").read_text(encoding="utf-8")
    files[Path("wiki.js")] = (SRC / "wiki.js").read_text(encoding="utf-8").replace(
        "/*@INDEX@*/[]", json.dumps(index, ensure_ascii=False, separators=(",", ":")))

    sitemap = None
    if INDEXABLE:
        sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                   + "".join("  <url><loc>%s%s</loc></url>\n" % (SITE_URL, u) for u in sitemap_urls)
                   + "</urlset>\n")
    return files, sitemap


def main():
    check = "--check" in sys.argv[1:]
    files, sitemap = build()
    on_disk = {p.relative_to(OUT) for p in OUT.rglob("*") if p.is_file()} if OUT.exists() else set()
    stale = sorted(str(p) for p, text in files.items()
                   if not (OUT / p).exists() or (OUT / p).read_text(encoding="utf-8") != text)
    extra = sorted(str(p) for p in on_disk - set(files))
    sitemap_stale = (sitemap or None) != (SITEMAP.read_text(encoding="utf-8") if SITEMAP.exists() else None)
    if check:
        problems = ["changed: wiki/" + p for p in stale] + ["not generated: wiki/" + p for p in extra]
        if sitemap_stale:
            problems.append("sitemap.xml is out of date")
        if problems:
            print("Out of date; run python3 build.py\n  " + "\n  ".join(problems))
            return 1
        print("wiki/ is up to date (%d files)" % len(files))
        return 0
    for p, text in files.items():
        (OUT / p).parent.mkdir(parents=True, exist_ok=True)
        (OUT / p).write_text(text, encoding="utf-8")
    for p in extra:
        (OUT / p).unlink()
    for d in sorted((d for d in OUT.rglob("*") if d.is_dir()), key=lambda d: -len(d.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    if sitemap:
        SITEMAP.write_text(sitemap, encoding="utf-8")
    elif SITEMAP.exists():
        SITEMAP.unlink()
    print("Built %d files into wiki/ (%d changed, %d removed)%s"
          % (len(files), len(stale), len(extra), "; wrote sitemap.xml" if sitemap else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
