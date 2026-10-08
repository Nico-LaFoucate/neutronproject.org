---
title: Installing Collider
status: guide
sub: From a clean Linux machine to your first Adobe launch — the whole stack, end to end.
---

**Collider** is the graphical front door to the whole stack. One command, `neutron setup`, installs everything underneath it — the [Neutron](/wiki/neutron/) compatibility engine, its patched Wine runtime, the Mud Hut installer and Collider itself — and from then on you install and launch your Adobe apps from Collider. This page walks the whole thing end to end.

<div class="callout"><p class="k">Beta — read this first</p><p>Neutron is in beta. Tested on three machines, all CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs. It runs real work in testing, but it is <strong>not</strong> stable or validated across hardware, distributions, or app versions — and you must bring your own <strong>legally licensed</strong> Adobe software. Treat this as a preview of the intended experience, not a finished product.</p></div>

## Before you begin

You'll want these in place first:

- **A 64-bit Linux distribution with glibc 2.39 or newer**: Ubuntu 24.04 or later, Fedora 40 or later, current Arch, CachyOS or Manjaro, or openSUSE Tumbleweed.
- **A Wayland session.** X11 isn't supported.
- **KDE Plasma is the supported desktop.** Other Wayland desktops (GNOME, Sway, Hyprland) are untested; they may work, expect rough edges, [reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues).
- **A Vulkan-capable GPU with current drivers.** NVIDIA (with the open driver) is the tested path. AMD and Intel GPUs aren't validated yet; [reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues).
- **Python 3** and **cabextract**.
- **Your own licensed Adobe apps.** You sign in inside each app, the same as on Windows.
- **A display scale that's a Windows step** (100, 125, 150, 175, 200, 225, 250 or 300%). See [Choosing a display scale](/wiki/start/basics/display-scale/).
- **A few gigabytes of free disk** for the runtime, the environment, and your apps.

## Step 1 — Install Neutron

In a terminal:

<div class="codebox">curl -LO https://github.com/Nico-LaFoucate/neutron/releases/latest/download/neutron
python3 neutron setup</div>

`neutron setup` downloads neutron-wine and the Mud Hut installer from GitHub, Microsoft's Visual C++ runtimes, GDI+ and core fonts from Microsoft, and Adobe's Creative Cloud package from Adobe, and installs Collider with a menu entry. It may ask for your password once, to turn on ntsync, which makes the apps much faster.

If you started from the Collider app instead, its **Set up** button runs the same setup.

## Step 2 — Add your Adobe apps

Open **Neutron Collider** from your menu and go to its **Mud Hut** tab. Pick whichever matches how you already have your apps:

- **Copy from an existing Windows install** — point Mud Hut at a licensed Windows Adobe install (a dual-boot drive, a backup, or a mounted disc image) and copy the app in.
- **Install from an offline package** — use an offline Adobe installer package you already have.
- **Download from Adobe** — download straight from Adobe's servers. No sign-in is needed to install; you sign in later, inside the app.

Already have a Wine prefix with Adobe apps in it? Point Collider at it with **Choose existing…**.

Whichever you choose, you must own a valid license — **Neutron distributes no Adobe code.**

<div class="callout"><p class="k">One environment, full interoperability</p><p>All your apps share a single Adobe environment, so <strong>Dynamic Link</strong> keeps working between them — send a Premiere sequence to After Effects, round-trip a Photoshop layer, and so on.</p></div>

## Step 3 — Launch

Each installed app appears as a tile in your library. Click **Launch**. Collider quietly does the rest: it applies the native display fix, starts Adobe's background licensing and IPC services, and hands off to the app. When you close the app, Collider shuts those services back down.

## What Collider is handling for you

The point of the launcher is that everything the Neutron investigation figured out by hand happens automatically:

- One shared Adobe environment, so Dynamic Link works across the suite.
- Copying an app over from an existing Windows install (Mud Hut's **Copy from a Windows install** method).

What's planned but not built yet is listed under [Planned](/wiki/start/basics/planned/).

## Updating and uninstalling

`neutron update` (or **Update** in Collider's Preferences) updates everything and moves your prefixes to the new runtime. `neutron uninstall` (or **Uninstall…**) removes Neutron; it asks before deleting any prefix, and keeps them unless you say so. ntsync stays on.

## Where this stands

The apps furthest along are [Premiere Pro](/wiki/premiere/), [Photoshop](/wiki/photoshop/), and [Lightroom Classic](/wiki/lightroom/) — all beta, all doing real work in testing. After Effects, Illustrator, Media Encoder and Animate run too, but haven't yet carried a paid job. For the honest, current status of each, see the **Applications** section, or the [status board](/#status) on the home page.

Once Collider is installed and an app launches, head to [Running your first app](/wiki/start/basics/first-app/).
