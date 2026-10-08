---
title: The ten-second menu
status: fix
sub: Why Lightroom’s “Edit in Photoshop” hung — and how a quarter-second file read explains it.
---

In Lightroom Classic, opening **Photo → Edit In** took about **ten seconds** before the submenu appeared. No error, no spinner, no crash — the menu just froze, every single time. That "no error, just slow" shape is worth recognizing: it usually means something correct is happening, just far too many times.

## What was actually happening

Every Windows program carries a tiny tag inside it called a **version resource** — the "Product version 26.9.0.15" you see in a file's Properties. It is well under a kilobyte. When Lightroom builds its "Edit in Photoshop" menu, it reads that tag out of `Photoshop.exe` to label the item.

The catch was *how* Wine fetched it. To read that tiny tag, Wine loaded the **entire program into memory in "image" mode** — the heavyweight way Windows loads a program it is about to *run*, laying out every section at its correct address. Fine for a normal app. But **`Photoshop.exe` is 208 megabytes.** Laying all of that out to read a sub-kilobyte tag took ~60&nbsp;ms — done four times per lookup. That is roughly a quarter-second.

The reason it became *ten* seconds: Lightroom re-checks this every time it validates the menu, and opening the submenu triggers validation about **forty times**.

## The fix

There is a lightweight way to open a file just to read data out of it — "as a data file." Nothing is laid out in advance; only the bytes you touch are read. We switched Wine's version-info code to that mode, after proving both modes return **byte-for-byte identical** data:

<div class="metrics"><div class="mhead">Reading Photoshop.exe’s version — measured</div><div class="mrow slow"><span class="lbl">Before — “image” mapping</span><span class="val">121.7 ms</span><span class="delta">&nbsp;</span></div><div class="mrow"><span class="lbl">After — “data file” mapping</span><span class="val">0.42 ms</span><span class="delta">288× faster</span></div><div class="mrow"><span class="lbl">Edit-In submenu open</span><span class="val">~10 s → ~0.1 s</span><span class="delta">gone</span></div></div>

Same version out, same everything — the menu just opens instantly now. The change lives in Wine itself, so it speeds up anything that reads version info from a large file. Shipped in runtime `11.10-12`.

<div class="callout"><p class="k">Diagnose this class yourself</p><p>If an Adobe app <em>pauses</em> with no error while building a menu or a picker — especially anything that detects other installed apps — suspect repeated reads of a large binary. Launch with <code>WINEDEBUG=+timestamp,+file</code> and watch for the same big <code>.exe</code> opened over and over, with tens-of-ms gaps, right where it hangs. The gaps are the cost; the repetition is the multiplier.</p></div>
