---
title: Adobe apps on Linux: common questions
status: guide
sub: Short answers about running Photoshop, Premiere Pro and the other Adobe apps on Linux with Neutron.
description: Can you run Adobe Photoshop, Premiere Pro and After Effects on Linux? Short answers on Neutron: requirements, GPUs, updates, plugins and cost.
schema: faq
---

### Can you run Adobe Photoshop and Premiere Pro on Linux?

Yes, with Neutron. It runs Photoshop, Premiere Pro, After Effects, Illustrator, Lightroom Classic, Media Encoder and Animate on Creative Cloud 2026 and 2025, plus Audition and InDesign on 2026 through experimental profiles. Neutron is in beta; the [status board](/#status) shows where each app stands.

### Do I need Windows or a virtual machine?

No. The apps run directly on Linux in Neutron's Wine runtime, with GPU acceleration.

### Do I need an Adobe subscription?

Yes. Bring your own Adobe subscription and sign in to your own Adobe account inside the apps. Neutron distributes no Adobe code.

### How do I install the Adobe apps?

[Install Collider](/wiki/start/basics/install-collider/), then install apps from its Mud Hut tab. Mud Hut downloads them from Adobe and installs them with Adobe's own installer. You don't need the Creative Cloud app.

### Do Adobe updates work?

Yes. Collider checks for updates and updates apps in place, so your preferences, presets, plugins and sign-in stay as they are. It keeps the old version and puts it back if an update fails, and it labels Adobe builds Neutron hasn't tested yet.

### Which Linux distributions and desktops work?

Neutron is developed and tested on CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs. Users also run it on Fedora, Ubuntu, Bazzite, Nobara and Arch, under GNOME and Hyprland. You need a 64-bit distribution with glibc 2.39 or newer, and a Wayland session: X11 isn't supported.

### Does it work with AMD or Intel GPUs?

Partly. NVIDIA is the tested path. On AMD, Photoshop 2026 and Premiere Pro 2026 use the GPU (Premiere through AMD's ROCm OpenCL), and Illustrator 2026 runs. A user reports Premiere Pro and Photoshop working on Intel Iris Xe.

### Do plugins work?

Yes. Effects, panels, Photoshop and Illustrator plugins, UXP plugins, VST3 audio plugins and vendors' own Windows installers have each been tested. See [Installing plugins](/wiki/start/basics/plugins/).

### How is Neutron different from plain Wine?

Neutron's Wine carries more than 260 patches written for the Adobe apps, each documented with the test that proved it. Around it, Mud Hut installs and updates the apps, Collider launches and manages them, and the `neutron` command line sets up each app's environment.

### Is Neutron free?

Yes. Neutron is free and open source: Neutron and its Wine runtime are LGPL-2.1, and Collider and Mud Hut are Apache-2.0.

### Does Neutron modify Adobe's software?

Neutron never modifies Adobe's program files. It changes one display setting in Adobe's own preferences, and adds three compatibility flags to aescripts panels (the original is backed up).
