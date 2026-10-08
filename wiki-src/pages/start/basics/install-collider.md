---
title: Installing Collider
status: guide
sub: From a clean Linux machine to your first Adobe launch — the whole stack, end to end.
---

**Collider** is the graphical front door to the whole stack. You install one app, and it sets up everything underneath it — the [Neutron](/wiki/neutron/) compatibility engine, its patched Wine runtime, and a healthy Adobe environment — then installs and launches your Adobe apps. No terminal required. This page walks the whole thing end to end.

<div class="callout"><p class="k">Experimental alpha — read this first</p><p>Neutron is early research. Tested on three machines, all CachyOS with KDE Plasma (Wayland) and NVIDIA GPUs. It runs real work in testing, but it is <strong>not</strong> stable or validated across hardware, distributions, or app versions — and you must bring your own <strong>legally licensed</strong> Adobe software. Treat this as a preview of the intended experience, not a finished product.</p></div>

## Before you begin

You'll want these in place first:

- **A modern Linux distribution** — CachyOS, Arch, or Ubuntu 22.04+. KDE on **Wayland** is the reference desktop.
- **A Vulkan-capable GPU with current drivers.** NVIDIA (with the open driver) is the tested path. AMD and Intel GPUs aren't validated yet; [reports welcome](https://github.com/Nico-LaFoucate/Neutron/issues).
- **A valid Adobe Creative Cloud subscription** — or an existing Adobe installation you can copy from.
- **A few gigabytes of free disk** for the runtime, the environment, and your apps.

## Step 1 — Install Collider

Download the latest Collider release for your distribution and open it. Collider is an ordinary desktop application — there's nothing to configure yet.

On first launch it runs a **plain-English compatibility check**: it looks at your GPU, driver, and desktop session and tells you, in words, whether your system is ready — and what to change if it isn't.

<div class="callout"><p class="k">During the alpha</p><p>The graphical Collider installer is still being finalized. Until it lands, the stack is driven directly through the Neutron command line. If you want to try it today, start from the <a class="ln" href="/wiki/neutron/">Neutron engine</a> pages or the project's repository for the current developer-preview steps.</p></div>

## Step 2 — Let Collider set up Neutron

Collider is the cockpit; **Neutron is the engine**. The first time you use it, Collider fetches and verifies the Neutron engine and its patched Wine runtime — the compatibility layer that makes Adobe apps run — and prepares a clean, Adobe-ready environment (a *prefix*). This happens automatically, and only once.

Under the hood this is the same work the `neutron` command line does — download and checksum the runtime, then provision the environment with the right fonts, libraries, and display settings — but you never touch a terminal. When it finishes, the compatibility check turns green.

## Step 3 — Add your Adobe apps

With the engine ready, add the apps you own. Collider is designed to support several ways to get Adobe software in — pick whichever matches how you already have it:

- **Download from Adobe** — download straight from Adobe's servers. No sign-in is needed to install; you sign in later, inside the app.
- **Copy from Windows** — point Collider at an existing Windows install (a dual-boot drive, a backup, or a mounted disc image) and it migrates the app in place.
- **Offline installer** — use an offline Adobe installer package you already have.
- **Import a prefix** — bring an app in from an existing Proton or Wine prefix.

Whichever you choose, you must own a valid license — **Neutron distributes no Adobe code.**

<div class="callout"><p class="k">One environment, full interoperability</p><p>All your apps share a single Adobe environment, so <strong>Dynamic Link</strong> keeps working between them — send a Premiere sequence to After Effects, round-trip a Photoshop layer, and so on.</p></div>

## Step 4 — Launch

Each installed app appears as a tile in your library. Click **Launch**. Collider quietly does the rest: it applies the native display fix, starts Adobe's background licensing and IPC services, and hands off to the app. When you close the app, Collider shuts those services back down.

## What Collider is handling for you

The point of the launcher is that everything the Neutron investigation figured out by hand happens automatically:

- One shared Adobe environment, so Dynamic Link works across the suite.
- Snapshot and rollback before updates, and **update gating** — Adobe updates are held until Neutron confirms the new version still works.
- Per-app GPU, display (Wayland / XWayland), and color controls.
- One-click migration from an existing Windows installation.

## Where this stands

The apps furthest along are [Premiere Pro](/wiki/premiere/), [Photoshop](/wiki/photoshop/), and [Lightroom Classic](/wiki/lightroom/) — all alpha, all doing real work in testing. After Effects is now usable too — its composition viewer renders and the canvas keeps pace; others are experimental. For the honest, current status of each, see the **Applications** section, or the [status board](/#status) on the home page.

Once Collider is installed and an app launches, head to [Running your first app](/wiki/start/basics/first-app/).
