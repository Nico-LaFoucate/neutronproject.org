---
title: What Neutron does today
status: guide
sub: Everything on this page has been tested, or says it's a user report.
description: Run Adobe Photoshop, Premiere Pro, After Effects, Illustrator and Lightroom Classic on Linux: installed from Adobe, GPU acceleration, pen tablets and plugins.
---

Neutron runs the Adobe Creative Cloud apps on Linux. You install them straight from Adobe, sign in with your own account, and work the way you would on Windows. This page lists what that covers today. The [status board](/#status) has the detail for each app, and [Known issues](/wiki/start/help/known-issues/) lists what still goes wrong.

## The apps

- **Premiere Pro, Photoshop, After Effects, Illustrator, Lightroom Classic, Media Encoder and Animate** run on Creative Cloud 2026 and 2025.
- **Audition and InDesign** run on 2026 through experimental profiles.
- **Dynamic Link** works both ways between Premiere Pro and After Effects.
- Premiere Pro, Photoshop and Lightroom Classic have been used for paid client work. After Effects has been used for day-to-day work.

More on each: [Photoshop](/wiki/photoshop/status/overview/), [Premiere Pro](/wiki/premiere/status/overview/), [After Effects](/wiki/aftereffects/status/overview/) and [Lightroom Classic](/wiki/lightroom/status/overview/) on Linux, and [common questions](/wiki/start/help/faq/).

## Installing and updating

- **Straight from Adobe.** Mud Hut downloads an app from Adobe and installs it with Adobe's own installer. It can also install from an offline package or `.iso`, or copy an existing Windows install. You don't need the Creative Cloud app.
- **Updates that keep your setup.** Collider checks for Adobe updates when it starts and once a day while it's open, and updates apps in place, so your preferences, presets, plugins and sign-in stay as they are. **Update all** installs every tested update in a prefix.
- **A way back.** Before each update, the old version is kept and put back automatically if anything fails. You can roll back later, too.
- **Tested builds first.** Neutron publishes a signed list of the Adobe builds it has tested, and new installs use the newest tested build. A newer build is labeled "Not yet tested by Neutron", and you can still choose it.

## Working the way you do on Windows

- **GPU acceleration.** Premiere Pro renders on NVIDIA GPUs through CUDA and exports with NVENC hardware encoding. Photoshop draws its canvas on the GPU. On AMD, Photoshop and Premiere Pro 2026 use the GPU. A user reports Premiere Pro and Photoshop working on Intel Iris Xe.
- **Pen tablets.** Pressure, tilt, the eraser and the pen's side buttons.
- **Two screens at different scales**, for example a 175% main screen next to a 100% pen display. Rotated screens work too.
- **Drag and drop** files from your file manager into the apps.
- **Copy and paste images** between the Adobe apps and Linux apps, in both directions.
- **Plugins.** Effects, panels, Photoshop and Illustrator plugins, UXP plugins, VST3 audio plugins and vendors' own Windows installers, from Collider's Plugins page. Every kind has been tested: see [Installing plugins](/wiki/start/basics/plugins/).
- **Lightroom Classic** imports from SD cards, and its masking, AI Denoise and Edit in Photoshop work.

## Where it runs

Neutron is developed and tested on CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs. Users also run it on Fedora, Ubuntu, Bazzite, Nobara and Arch, under GNOME and Hyprland.

## How it's built

- **Fixes go into the engine.** When an Adobe app misbehaves, the fix goes into Neutron's own Wine, which carries more than 260 patches written for these apps. Each one is documented with the test that proved it. Because the fix lives in Wine, Adobe's next update doesn't undo it.
- **Adobe's files are left alone.** Neutron never modifies Adobe's program files. It changes one display setting in Adobe's own preferences, and adds three compatibility flags to aescripts panels (the original is backed up).
- **Open source and free.** Neutron and its Wine runtime are LGPL-2.1; Collider and Mud Hut are Apache-2.0.

## How fast it moves

Since its first public release on October 8, 2026: 113 releases across Neutron, its Wine runtime, Collider and Mud Hut, and 25 reported issues closed (as of October 27).

Neutron is free. If it helps your work, you can [support it](/#support).
