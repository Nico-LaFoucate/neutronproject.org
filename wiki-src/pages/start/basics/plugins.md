---
title: Installing plugins
status: guide
sub: Third-party plugins, extension panels, scripts and audio plugins, from Collider or a terminal.
---

Neutron puts each plugin where its Windows installer would, inside the prefix your Adobe apps run from. Hand it the plugin files, an extension package, a script, or the vendor's own Windows installer. This needs Neutron 1.0.0-beta.29 and Collider 0.1.12 or newer.

## In Collider

<ol>
<li>Open <strong>Plugins</strong> in the sidebar, under Library. It works on the prefix selected on the <strong>Prefixes</strong> tab.</li>
<li>Drop plugin files or folders onto the page, or use <strong>Choose files…</strong> or <strong>Choose a folder…</strong>.</li>
<li>Each item gets a line: green when it's installed, red with the reason when it isn't.</li>
<li>Restart the Adobe app to load what you added.</li>
</ol>

**Scripts** (`.jsx`, `.jsxbin`): Collider asks which app the script is for.

**A vendor's installer** (`.exe`, `.msi`): close the Adobe apps first. The installer opens its own window; click through it as you would on Windows. Collider waits until the installer and anything it opens afterward (a readme, for example) have closed.

The page also lists what the prefix already holds, and has an **Open folder** button for each plugin folder, so you can add a plugin by hand.

## From a terminal

<div class="codebox">neutron plugins install &lt;file or folder&gt;...
neutron plugins install --app aftereffects MyPanel.jsx
neutron plugins list
neutron plugins folder</div>

They work on the prefix selected in Collider; add `--prefix <path>` to pick another. `neutron plugins folder` prints the Linux path of each plugin folder.

## Where each kind goes

All inside the prefix:

- **`.aex` or `.prm` files, or a folder of them:** `Program Files\Adobe\Common\Plug-ins\7.0\MediaCore`, shared by After Effects, Premiere Pro and Media Encoder.
- **Photoshop plugin files** (`.8bf` and the other `.8b*` types): Photoshop's `Plug-ins` folder.
- **`.aip` files:** Illustrator's `Plug-ins` folder.
- **An extension package (`.zxp`):** `Program Files (x86)\Common Files\Adobe\CEP\extensions`, in a folder named after the extension.
- **A script (`.jsx`, `.jsxbin`):** the scripts folder of the app you choose (for After Effects, `ScriptUI Panels`).
- **A VST3 plugin (`.vst3` file or folder):** `Program Files\Common Files\VST3`.
- **A vendor's installer (`.exe`, `.msi`):** wherever the installer puts it.

If a plugin is already there, the new one replaces it.

## Audio plugins in Premiere Pro

Premiere Pro finds new audio plugins only on its very first launch. After you install one, with the vendor's installer or as a `.vst3`, load it:

<ol>
<li>In Premiere Pro, choose <strong>Edit &gt; Preferences &gt; Audio</strong>, then <strong>Manage Audio Plug-ins…</strong>.</li>
<li>Click <strong>Scan for Plug-Ins</strong>. The plugin appears in the list with its status.</li>
<li>Click <strong>OK</strong>. It's now under <strong>Effects &gt; Audio Effects &gt; VST3</strong>.</li>
</ol>

Tested with FabFilter's Windows installer: Pro-Q 4 installed, passed Premiere's scan, and processed audio on a clip with its own interface open.

## Extension packages (.zxp)

Neutron checks a package's signature before it installs it. A damaged package is refused, and the extension that was already installed stays as it was.

A package that isn't signed at all is installed with a note: the Adobe apps refuse to load it unless PlayerDebugMode is on, and its developer's instructions say how to turn that on.

## Not supported yet

- **UXP plugins** (`.ccx`): these are installed by Adobe's own plugin installer, which doesn't work in Neutron prefixes yet.
- **Loose VST2 files** (`.dll`): there's no single standard VST2 folder, so Neutron doesn't place them. A vendor's installer that includes VST2 plugins still puts them where it wants.
- **The aescripts + aeplugins manager** runs, but installing plugins through it hasn't been tested yet.

If a plugin won't activate, or keeps asking to be activated again, see [Troubleshooting](/wiki/start/help/troubleshooting/).
