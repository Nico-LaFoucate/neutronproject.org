---
title: Installing Collider
status: guide
sub: From a clean Linux machine to your first Adobe launch — the whole stack, end to end.
description: Install Neutron on Linux and get Adobe Photoshop, Premiere Pro and the other Creative Cloud apps running: requirements and steps, end to end.
---

**Collider** is the graphical front door to the whole stack. Download it, click **Set up**, and it installs everything underneath it — the [Neutron](/wiki/neutron/) compatibility engine, its patched Wine runtime and the Mud Hut installer — with no terminal needed. From then on you install and launch your Adobe apps from Collider. This page walks the whole thing end to end.

<div class="callout"><p class="k">Beta — read this first</p><p>Neutron is in beta. It's developed and tested on CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs, and users also run it on Fedora, Ubuntu, Bazzite, Nobara and Arch, under GNOME and Hyprland as well as KDE. AMD GPUs are partly tested (see below); on Intel GPUs, a user reports Premiere Pro and Photoshop working. Things break, and you must bring your own <strong>legally licensed</strong> Adobe software.</p></div>

## Before you begin

You'll want these in place first:

- **A 64-bit Linux distribution with glibc 2.39 or newer**: Ubuntu 24.04 or later, Fedora 40 or later, current Arch, CachyOS or Manjaro, or openSUSE Tumbleweed.
- **A Wayland session, or X11 (experimental).** Neutron is made for Wayland. X11 sessions, such as Linux Mint's default, run with experimental support: Neutron's fixes for Wayland are off there.
- **KDE Plasma, GNOME or Hyprland.** Neutron is developed on KDE Plasma, and users also run it under GNOME and Hyprland. [Reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues) from other desktops.
- **A Vulkan-capable GPU with current drivers.** NVIDIA (with the open driver) is the tested path. On AMD, Photoshop 2026 and Premiere Pro 2026 use the GPU and Illustrator 2026 runs; Premiere needs AMD's ROCm OpenCL (`neutron doctor` checks for it). Hardware video encoding on AMD is new and testers haven't confirmed it yet; on Fedora and openSUSE it needs the full Mesa from RPM Fusion or Packman. On Intel, a user reports Premiere Pro and Photoshop working on an 11th-gen Iris Xe with Intel's OpenCL runtime and media driver installed (on Fedora: `intel-opencl intel-compute-runtime intel-media-driver`). [Reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues).
- **32-bit (multilib) system and graphics libraries**: Adobe's apps start 32-bit helper processes. If the 32-bit C library is missing, setup installs it for you.
- **Python 3** and **cabextract**. If cabextract is missing, setup installs it for you.
- **Your own licensed Adobe apps.** You sign in inside each app, the same as on Windows.
- **A display scale that's a Windows step** (100, 125, 150, 175, 200, 225, 250 or 300%). See [Choosing a display scale](/wiki/start/basics/display-scale/).
- **Free disk space:** About 8 GB, plus your Adobe apps.

## Step 1 — Install Neutron

<p><a class="dl" href="https://github.com/Nico-LaFoucate/Collider/releases/latest/download/Collider-x86_64.AppImage">Download Collider</a></p>

Then open the file you downloaded, `Collider-x86_64.AppImage`, from the Downloads folder in your file manager. On GNOME, Cinnamon and COSMIC, clicking it in your browser's download list won't start it.

- **KDE Plasma:** in Dolphin, double-click the file, then click **Launch** and **Continue**.
- **GNOME (Ubuntu, Fedora Workstation):** in Files, right-click the file, choose **Properties** and turn on **Executable as Program**. Close the window, then double-click the file.
- **Cinnamon (Linux Mint):** in the file manager, right-click the file, choose **Properties**, open **Permissions** and tick **Allow executing file as program**. Close the window, then double-click the file.
- **COSMIC (Pop!_OS):** in COSMIC Files, double-click the file and click **Set and launch**.

Collider opens. Click **Set up**. If your system is missing packages Neutron needs, Collider shows what it will install and the exact command, with an **Install and continue** button. Your system asks for your password once, and setup carries on. If ntsync is off, the same step turns it on; it makes the apps much faster.

Setup downloads neutron-wine and the Mud Hut installer from GitHub, Microsoft's Visual C++ runtimes and GDI+ from Microsoft, Microsoft's core fonts (their original installers, from a pinned mirror), and Adobe's Creative Cloud package from Adobe. When it's done, Collider is in your app menu and you can delete the file you downloaded.

### Or in a terminal

<div class="codebox">curl -LO https://github.com/Nico-LaFoucate/neutron/releases/latest/download/neutron
python3 neutron setup</div>

`neutron setup` does the same and installs Collider with a menu entry. If packages are missing, it shows the command and asks before installing them. It may ask for your password once.

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

The apps furthest along are [Premiere Pro](/wiki/premiere/), [Photoshop](/wiki/photoshop/), and [Lightroom Classic](/wiki/lightroom/) — all beta, all used for paid client work. After Effects and Media Encoder have been used for paid client work too, and Illustrator, Animate, Audition and InDesign run. For the honest, current status of each, see the [status board](/#status) on the home page.

Once Collider is installed and an app launches, head to [Running your first app](/wiki/start/basics/first-app/).
