---
title: Press kit
status: guide
sub: Facts, screenshots and logos for writing about Neutron. Everything here has been tested. Checked October 28, 2026.
description: The Neutron press kit: what it is, which Adobe apps it runs on Linux, the tested setups, screenshots, logos and contact, for journalists and creators.
---

Neutron runs Adobe's Creative Cloud apps on Linux: Photoshop, Premiere Pro, After Effects, Illustrator, Lightroom Classic, Media Encoder and Animate. You install the apps straight from Adobe and sign in with your own account. Neutron is free, open source and in beta.

<div class="press-quote"><p>I'm Nico LaFoucate, I'm a creative of over 10 years. You might know me as one of the talents involved with Smack Studio on YouTube. I decided to swear off of Windows entirely two years ago because of its increasingly worse user experience. I have been a long-time tinkerer of Wine and a daily driver of Linux for the past two years. After I lost my full-time job, I needed to be able to use my own computer to do client work. It was out of this necessity that Neutron was born.</p><p class="by">Nico LaFoucate, creator of Neutron</p></div>

## Fact sheet

<div class="facts">
<div class="fr"><div class="fk">Name</div><div class="fv">Neutron. Where the name could be confused with iZotope Neutron (an audio plugin) or OpenStack Neutron (cloud networking): “Neutron, the Adobe-on-Linux compatibility layer”.</div></div>
<div class="fr"><div class="fk">Made by</div><div class="fv">Nico LaFoucate and Ficus Media Group. An independent project, not affiliated with or endorsed by Adobe.</div></div>
<div class="fr"><div class="fk">First public release</div><div class="fv">October 8, 2026</div></div>
<div class="fr"><div class="fk">Status</div><div class="fv">Beta</div></div>
<div class="fr"><div class="fk">Price</div><div class="fv">Free. You need your own Adobe subscription.</div></div>
<div class="fr"><div class="fk">Apps</div><div class="fv">Photoshop, Premiere Pro, After Effects, Illustrator, Lightroom Classic, Media Encoder and Animate, on Creative Cloud 2026 and 2025. Dynamic Link works both ways between Premiere Pro and After Effects. Audition and InDesign run on 2026. Lightroom (the cloud app) is planned. <a class="ln" href="/#status">Status board</a></div></div>
<div class="fr"><div class="fk">Used for paid client work</div><div class="fv">Premiere Pro, Photoshop, Lightroom Classic, After Effects and Media Encoder</div></div>
<div class="fr"><div class="fk">Adobe builds tested</div><div class="fv">Each one listed with the date it was tested: <a class="ln" href="/wiki/start/basics/tested-builds/">Tested Adobe builds</a></div></div>
<div class="fr"><div class="fk">The three parts</div><div class="fv"><strong>Neutron</strong>, the engine, with its own Wine runtime and a command line. <strong>Collider</strong>, the desktop app that sets everything up and launches the apps. <strong>Mud Hut</strong>, the installer that gets the apps from Adobe and keeps them updated.</div></div>
<div class="fr"><div class="fk">How it's made</div><div class="fv">Neutron is built with assistance from AI tools. However, every change and fix is proposed, tested and signed off on by human hands.</div></div>
<div class="fr"><div class="fk">Under the hood</div><div class="fv">Neutron's own Wine (Wine 11.10 with Staging and ntsync) carrying more than 260 patches written for these apps, plus DXVK and vkd3d-proton. Every patch is public and documented with the test that proved it.</div></div>
<div class="fr"><div class="fk">Developed on</div><div class="fv">CachyOS, KDE Plasma (Wayland). Users also run it on Fedora, Ubuntu, Bazzite, Nobara and Arch, under GNOME and Hyprland.</div></div>
<div class="fr"><div class="fk">Setup without a terminal</div><div class="fv">Tested on Fedora 44 (KDE Plasma), Ubuntu 26.04 (GNOME), Linux Mint 22.3 (Cinnamon) and Pop!_OS 24.04 (COSMIC)</div></div>
<div class="fr"><div class="fk">GPUs</div><div class="fv">NVIDIA, AMD and Intel. On NVIDIA, Premiere Pro renders through CUDA and exports with NVENC. On AMD, Photoshop and Premiere Pro 2026 use the GPU. On Intel, Premiere Pro runs very well and Photoshop works on Iris Xe graphics.</div></div>
<div class="fr"><div class="fk">Desktop sessions</div><div class="fv">Wayland. X11 sessions run with experimental support.</div></div>
<div class="fr"><div class="fk">Pace</div><div class="fv">122 releases across Neutron, its Wine runtime, Collider and Mud Hut since October 8, and 25 reported issues closed (as of October 28, 2026)</div></div>
<div class="fr"><div class="fk">Licenses</div><div class="fv">Neutron and its Wine runtime: LGPL-2.1-or-later. Collider and Mud Hut: Apache-2.0.</div></div>
<div class="fr"><div class="fk">Source</div><div class="fv"><a class="ln" href="https://github.com/Nico-LaFoucate/Neutron">Neutron</a> · <a class="ln" href="https://github.com/Nico-LaFoucate/neutron-wine">neutron-wine</a> · <a class="ln" href="https://github.com/Nico-LaFoucate/Collider">Collider</a> · <a class="ln" href="https://github.com/Nico-LaFoucate/Mud-Hut">Mud Hut</a></div></div>
</div>

## What it does

- **Installs and updates the apps straight from Adobe**, with Adobe's own installer. The Creative Cloud app isn't needed. Updates keep your preferences, presets, plugins and sign-in, and the old version is kept in case anything fails.
- **Runs on NVIDIA, AMD and Intel GPUs.** Photoshop and Premiere Pro use the GPU on NVIDIA and AMD. On NVIDIA, Premiere Pro renders through CUDA and exports with NVENC hardware encoding.
- **Pen tablets:** pressure, tilt, the eraser and the pen's side buttons.
- **Two screens at different scales**, such as a 175% main screen next to a 100% pen display.
- **Drag and drop** from the file manager, and **copy and paste images** between the Adobe apps and Linux apps, both ways.
- **Plugins:** effects, panels, Photoshop and Illustrator plugins, UXP plugins, VST3 audio plugins and vendors' own Windows installers.
- **Lightroom Classic** imports from SD cards, and its masking, AI Denoise and Edit in Photoshop work.

The full list: [What Neutron does today](/wiki/start/basics/what-neutron-does/). What still goes wrong: [Known issues](/wiki/start/help/known-issues/).

## What it doesn't do

- **It doesn't include any Adobe software**, and it doesn't get around Adobe's licensing. You need your own Adobe subscription and sign in with your own account.
- **It doesn't modify Adobe's program files.** Fixes go into Neutron's own Wine, so Adobe's next update doesn't undo them.
- **It isn't an Adobe product.** Adobe doesn't make, support or endorse Neutron.

## Screenshots

Click any screenshot for the full-size PNG. All shown on KDE Plasma (Wayland).

### The Adobe apps

<div class="shots">
<figure><a href="/press/media/photoshop-2026.png"><img src="/press/media/photoshop-2026-1920.jpg" alt="Photoshop 2026 with a landscape photo open and two Curves adjustment layers" loading="lazy" width="1920" height="1052"></a><figcaption>Photoshop 2026 (27.11) with a Curves adjustment layer. Neutron runtime 11.10-157.</figcaption></figure>
<figure><a href="/press/media/premiere-pro-2026.png"><img src="/press/media/premiere-pro-2026-1920.jpg" alt="Premiere Pro 2026 editing a sequence of four clips, with a clip's properties open" loading="lazy" width="1920" height="1082"></a><figcaption>Premiere Pro 2026 (26.5.2): a four-clip sequence on the timeline. Neutron runtime 11.10-157.</figcaption></figure>
<figure><a href="/press/media/after-effects-2026.png"><img src="/press/media/after-effects-2026-1920.jpg" alt="After Effects 2026 with a waterfall composition and a title layer" loading="lazy" width="1920" height="1052"></a><figcaption>After Effects 2026 (26.5): a composition with a title layer. Neutron runtime 11.10-158.</figcaption></figure>
<figure><a href="/press/media/lightroom-classic.png"><img src="/press/media/lightroom-classic-1920.jpg" alt="Lightroom Classic in the Develop module with a landscape photo and its histogram" loading="lazy" width="1920" height="1052"></a><figcaption>Lightroom Classic (15.6) in the Develop module. Neutron runtime 11.10-158.</figcaption></figure>
<figure><a href="/press/media/illustrator-2026.png"><img src="/press/media/illustrator-2026-1920.jpg" alt="Illustrator 2026 with a layout: a placed landscape photo, a title and a green circle" loading="lazy" width="1920" height="1052"></a><figcaption>Illustrator 2026 (30.8): a layout with a placed photo, type and a vector shape. Neutron runtime 11.10-158.</figcaption></figure>
<figure><a href="/press/media/indesign-2026.png"><img src="/press/media/indesign-2026-1920.jpg" alt="InDesign 2026 with a page: a mountain photo, a headline and a caption" loading="lazy" width="1920" height="1052"></a><figcaption>InDesign 2026 (21.6): a page with a placed photo, a headline and a caption. Neutron runtime 11.10-158.</figcaption></figure>
<figure><a href="/press/media/media-encoder-2026.png"><img src="/press/media/media-encoder-2026-1920.jpg" alt="Media Encoder 2026 with four clips exported to H.264, each marked Done" loading="lazy" width="1920" height="1052"></a><figcaption>Media Encoder 2026 (26.5.2): four clips exported to H.264. Neutron runtime 11.10-158.</figcaption></figure>
<figure><a href="/press/media/audition-2026.png"><img src="/press/media/audition-2026-1920.jpg" alt="Audition 2026 editing a stereo waveform with a selection" loading="lazy" width="1920" height="1052"></a><figcaption>Audition 2026 (26.5) editing a stereo recording. Neutron runtime 11.10-158.</figcaption></figure>
</div>

Adobe product screenshots reprinted with permission from Adobe. The photos and footage in them are public domain or CC0, from Wikimedia Commons; the audio in Audition was made for this page.

### Collider

<div class="shots">
<figure><a href="/press/media/collider-library.png"><img src="/press/media/collider-library.png" alt="Collider's library: every Adobe app in a prefix, each with a Launch button" loading="lazy" width="1925" height="1260"></a><figcaption>Collider's library: each installed Adobe app, ready to launch.</figcaption></figure>
<figure><a href="/press/media/collider-first-run.png"><img src="/press/media/collider-first-run.png" alt="Collider's first-run setup panel, offering to install two system packages" loading="lazy" width="1925" height="1260"></a><figcaption>First run: Collider sets Neutron up without a terminal. When the system lacks a package Neutron needs, it shows the exact command and asks for the password once. An Arch-based system is shown.</figcaption></figure>
<figure><a href="/press/media/collider-mudhut.png"><img src="/press/media/collider-mudhut.png" alt="Mud Hut inside Collider, with four ways to install Adobe apps" loading="lazy" width="1925" height="1260"></a><figcaption>Mud Hut, the installer: download from Adobe, install from an offline package, copy a Windows install, or update installed apps.</figcaption></figure>
<figure><a href="/press/media/collider-plugins.png"><img src="/press/media/collider-plugins.png" alt="Collider's Plugins page listing an extension panel, an effect plugin and a VST3 plugin" loading="lazy" width="1925" height="1260"></a><figcaption>The Plugins page: drop in plugin files, UXP plugins, extension packages or a vendor's installer. Shown: Captioneer, Gyroflow and FabFilter Pro-Q 4 (VST3).</figcaption></figure>
</div>

Collider 0.1.17 with the neutron CLI 1.0.0-beta.35.

## Video

<div class="press-todo"><p class="k">To fill: clips</p><p>One or two 30 to 90 second clips of the apps at work.</p></div>

**Coverage:** [The Linux Experiment](https://www.youtube.com/watch?v=eAeT63x338Y&t=203s) covered Neutron on October 10, 2026.

## Logos

PNG with a transparent background, 800 × 800 (the app icon is 1024 × 1024). Click to download. They're free to use in articles, videos and links promoting Neutron.

<div class="logos">
<a class="logo light" href="/press/logos/neutron-logo-black.png"><img src="/press/logos/neutron-logo-black.png" alt="Neutron logo, black" loading="lazy"><span>Neutron, black</span></a>
<a class="logo dark" href="/press/logos/neutron-logo-white.png"><img src="/press/logos/neutron-logo-white.png" alt="Neutron logo, white" loading="lazy"><span>Neutron, white</span></a>
<a class="logo light" href="/press/logos/collider-logo-black.png"><img src="/press/logos/collider-logo-black.png" alt="Collider logo, black" loading="lazy"><span>Collider, black</span></a>
<a class="logo dark" href="/press/logos/collider-logo-white.png"><img src="/press/logos/collider-logo-white.png" alt="Collider logo, white" loading="lazy"><span>Collider, white</span></a>
<a class="logo light" href="/press/logos/collider-app-icon-1024.png"><img src="/press/logos/collider-app-icon-1024.png" alt="Collider app icon" loading="lazy"><span>Collider app icon</span></a>
</div>

## Contact

Press and interviews: **contact@neutronproject.org**

Adobe, Photoshop, Premiere Pro, After Effects, Illustrator, Lightroom, Media Encoder, Animate, Audition and InDesign are trademarks of Adobe Inc.
