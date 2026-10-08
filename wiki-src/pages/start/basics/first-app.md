---
title: Running your first app
status: guide
sub: You clicked Launch — here’s what to expect, and how to get to real work.
---

You've [installed Collider](/wiki/start/basics/install-collider/), added an app, and hit **Launch**. Collider has already applied the display fix and started Adobe's background services — so from here, it should feel like the app you already know. Here's what to expect on that first run, and how to get to actual work.

## First launch: sign in to Adobe

The app opens to its normal Adobe home screen. The first time, it asks you to **sign in with your Adobe ID** — the same Creative Cloud account you'd use on Windows or macOS. This is what activates your license; Neutron doesn't replace or bypass it.

Sign-in happens in an embedded browser window, so give it a moment to load. You only do this once — Collider is designed to keep you signed in across the whole suite, so the next app you open is already authenticated.

<div class="callout"><p class="k">You bring the license</p><p>Neutron distributes no Adobe software and circumvents nothing. You run the genuine app, signed into your own valid subscription.</p></div>

## What “working” looks like

Each app behaves like its Windows counterpart. Quick starts for the three that are furthest along — all **alpha**, all doing real work in testing:

### Premiere Pro

Import your media, cut on the timeline, and play back in the program monitor. GPU and CUDA (Mercury) acceleration are on, and export encodes with hardware **NVENC** and muxes into valid MP4 files **natively** — no extra steps at export time. See the [Premiere page](/wiki/premiere/).

### Photoshop

**File → New** brings up the full workspace — canvas and panels docked — and drawing goes straight to the GPU. There's some warm-up lag and the occasional redraw artifact; details on the [Photoshop page](/wiki/photoshop/).

### Lightroom Classic

Import your RAW files — drag in a folder or plug in an SD card — then develop with GPU acceleration, run **AI Denoise**, and round-trip to Photoshop with **Edit In**. See the [Lightroom page](/wiki/lightroom/) for what's confirmed working.

## Getting your files in and out

Your Linux home folder is available inside the app's open and save dialogs, so you can point at the same media and save projects to the same places you'd use natively. Keep working files on a fast local disk for the best performance — the app is reading and writing through the compatibility layer, and a slow network share will feel slow.

## GPU, export, and the helpers you don’t manage

GPU acceleration is on by default, and Collider keeps Adobe's licensing and IPC services alive while you work, shutting them down when you close the app. Video export needs no hand-holding: Premiere muxes its NVENC exports into valid MP4 files **natively**. (This used to need a muxing helper you pointed at the export path — a fix in Neutron's C-runtime layer removed that step entirely.)

## If something isn’t right

This is experimental alpha, so a few things are expected and a few are worth checking:

- **Some warm-up lag and occasional redraw artifacts are normal** right now, especially in the first moments after launch.
- **If an app won't start or the GPU isn't used,** re-run Collider's compatibility check — it calls out driver, GPU, or desktop-session problems in plain English.
- **For anything app-specific** — a feature that's greyed out, a panel that misbehaves — check that app's page under **Applications**; known issues and their status live there.
- **A given feature may simply not be validated yet.** The [status board](/#status) is the honest, current picture of what's been confirmed.

## Where to go next

Head into the **Applications** section for the current status, notable fixes, and known issues of each app — that's where the detail lives, and where new pages land as more of the suite comes online.
