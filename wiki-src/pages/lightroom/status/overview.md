---
title: Lightroom Classic on Linux
status: feature
sub: What works in Adobe Lightroom Classic on Linux with Neutron, and how to get it running.
description: Run Adobe Lightroom Classic on Linux with Neutron: large RAW imports, SD cards, AI Denoise, AI masking and Edit in Photoshop. Free and open source.
---

Neutron runs Adobe Lightroom Classic on Linux, installed straight from Adobe and signed in with your own Adobe account. It's in beta, stable for cataloging, developing and export, and it has been used for paid client work. Confirmed working:

- **Boots and imports at scale** — 1000+ RAW files imported at once, SD-card hotplug auto-detected. GPU auto-detected and enabled.
- **Develop performance** — smooth zoom and slider response (the earlier stepping is fixed).
- **AI features run natively** — Camera Raw *Denoise* (Photo → Enhance) and AI *masking* (Select Subject / Sky) both work.
- **Edit in Photoshop** — round-trips correctly, and the submenu opens instantly (see the [ten-second menu](/wiki/neutron/fixes/edit-in-lag/) fix).
- **Copy Settings, masking popups, filmstrip scrolling** across large catalogs — all working.
- **Batch export.**

The interface takes several seconds to paint in when the app starts; that comes from inside the app, not from Neutron. See [Known issues](/wiki/start/help/known-issues/).

## Get it running

[Install Collider](/wiki/start/basics/install-collider/), install Lightroom Classic from its Mud Hut tab, then see [Running your first app](/wiki/start/basics/first-app/).
