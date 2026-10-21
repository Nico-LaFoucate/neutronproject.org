---
title: Installing Collider
status: guide
sub: From a clean Linux machine to your first Adobe launch — the whole stack, end to end.
---

**Collider** is the graphical front door to the whole stack. One command, `neutron setup`, installs everything underneath it — the [Neutron](/wiki/neutron/) compatibility engine, its patched Wine runtime, the Mud Hut installer and Collider itself — and from then on you install and launch your Adobe apps from Collider. This page walks the whole thing end to end.

<div class="callout"><p class="k">Beta — read this first</p><p>Neutron is in beta. It's developed and tested on CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs, and users also run it on Ubuntu, Bazzite, Nobara and Arch, under GNOME and Hyprland as well as KDE. AMD GPUs are partly tested (see below); on Intel GPUs, a user reports Premiere Pro and Photoshop working. Things break, and you must bring your own <strong>legally licensed</strong> Adobe software.</p></div>

## Before you begin

You'll want these in place first:

- **A 64-bit Linux distribution with glibc 2.39 or newer**: Ubuntu 24.04 or later, Fedora 40 or later, current Arch, CachyOS or Manjaro, or openSUSE Tumbleweed.
- **A Wayland session.** X11 isn't supported.
- **KDE Plasma, GNOME or Hyprland.** Neutron is developed on KDE Plasma, and users also run it under GNOME and Hyprland. [Reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues) from other desktops.
- **A Vulkan-capable GPU with current drivers.** NVIDIA (with the open driver) is the tested path. On AMD, Photoshop 2026 and Premiere Pro 2026 use the GPU and Illustrator 2026 runs; Premiere needs AMD's ROCm OpenCL (`neutron doctor` checks for it). Hardware video encoding on AMD is new and testers haven't confirmed it yet; on Fedora and openSUSE it needs the full Mesa from RPM Fusion or Packman. On Intel, a user reports Premiere Pro and Photoshop working on an 11th-gen Iris Xe with Intel's OpenCL runtime and media driver installed (on Fedora: `intel-opencl intel-compute-runtime intel-media-driver`). [Reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues).
- **32-bit (multilib) system and graphics libraries**: Adobe's apps start 32-bit helper processes.
- **Python 3** and **cabextract**.
- **Your own licensed Adobe apps.** You sign in inside each app, the same as on Windows.
- **A display scale that's a Windows step** (100, 125, 150, 175, 200, 225, 250 or 300%). See [Choosing a display scale](/wiki/start/basics/display-scale/).
- **Free disk space:** About 8 GB, plus your Adobe apps.

## Step 1 — Install Neutron

In a terminal:

<div class="codebox">curl -LO https://github.com/Nico-LaFoucate/neutron/releases/latest/download/neutron
python3 neutron setup</div>

`neutron setup` downloads neutron-wine and the Mud Hut installer from GitHub, Microsoft's Visual C++ runtimes and GDI+ from Microsoft, Microsoft's core fonts (their original installers, from a pinned mirror), and Adobe's Creative Cloud package from Adobe, and installs Collider with a menu entry. It may ask for your password once, to turn on ntsync, which makes the apps much faster.

If you started from the Collider app instead, its **Set up** button runs the same setup.

## Step 2 — Add your Adobe apps

Open **Neutron Collider** from your menu and go to its **Mud Hut** tab. Pick whichever matches how you already have your apps:

- **Copy from an existing Windows install** — point Mud Hut at a licensed Windows Adobe install (a dual-boot drive, a backup, or a mounted C: drive) and copy the app in.
- **Install from an offline package** — use an offline Adobe installer package or an `.iso` disc image you already have.
- **Download from Adobe** — download straight from Adobe's servers. No sign-in is needed to install; you sign in later, inside the app.

Already have a Wine prefix with Adobe apps in it? Point Collider at it with **Choose existing…**.

Whichever you choose, you must own a valid license — **Neutron distributes no Adobe code.**

<div class="callout"><p class="k">Dynamic Link</p><p>Apps installed into the same prefix share one Adobe environment, so <strong>Dynamic Link</strong> works between Premiere Pro and After Effects, and either app can open the other.</p></div>

## Step 3 — Launch

Each installed app appears as a tile in your library. Click **Launch**. Collider quietly does the rest: it applies the native display fix and hands off to the app. When you close the app, Collider has Neutron clean up after it, so Adobe's leftover background processes can't wedge the next launch.

## What Collider is handling for you

The point of the launcher is that everything the Neutron investigation figured out by hand happens automatically:

- One shared Adobe environment per prefix, for Dynamic Link between Premiere Pro and After Effects.
- Copying an app over from an existing Windows install (Mud Hut's **Copy from an existing Windows install** method).
- Updating your Adobe apps through Adobe's own installer, with a backup that's put back if an update fails.

What's planned but not built yet is listed under [Planned](/wiki/start/basics/planned/).

## Updating and uninstalling

**Neutron:** `neutron update` (or **Update Neutron** in Collider's Preferences) updates everything and moves your prefixes to the new runtime.

**Your Adobe apps:** Collider checks for Adobe app updates when it starts and once a day while it's open. An app's card shows its update, and **Update all** updates every verified update in a prefix. Nothing updates on its own. Builds Neutron hasn't verified yet are marked "not yet verified" and need one more confirmation. Updates go through Adobe's own installer, so your preferences, presets, plugins and Adobe sign-in stay as they are. A backup is kept before each update and put back automatically if anything fails; **Preferences → Adobe app updates** turns the check or the backup off. A new yearly version installs beside the old one, with the option to remove the old one. Close the Adobe apps in a prefix before updating it.

**Uninstalling:** `neutron uninstall` (or **Uninstall…**) removes Neutron; it asks before deleting any prefix, and keeps them unless you say so. ntsync stays on.

## Where this stands

The apps furthest along are [Premiere Pro](/wiki/premiere/), [Photoshop](/wiki/photoshop/), and [Lightroom Classic](/wiki/lightroom/) — all beta, all used for paid client work. After Effects, Illustrator, Media Encoder, Animate, Audition and InDesign run too. For the honest, current status of each, see the [status board](/#status) on the home page.

Once Collider is installed and an app launches, head to [Running your first app](/wiki/start/basics/first-app/).
