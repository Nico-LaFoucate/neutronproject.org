---
title: What is Neutron?
status: guide
sub: The three pieces, in one minute.
---

Neutron is a **compatibility engine** that runs Adobe Creative Suite applications on Linux. It is built on Wine, DXVK, and vkd3d-proton, and patched specifically for the way Adobe applications talk to Windows.

It comes as three separate pieces, each owning one job:

- **[Neutron](/wiki/neutron/)** — the engine. Neutron-Wine plus DXVK, vkd3d-proton, a DirectComposition bridge, an nvcuda wrapper, and every Adobe-specific fix. Driven entirely through a command line; no GUI required.
- **[Collider](/wiki/collider/)** — the launcher. A desktop app that finds your installed apps, checks a prefix is healthy, launches it, and supervises it. It calls Neutron for anything compatibility-related and holds no fixes of its own.
- **[Mud Hut](/wiki/mudhut/)** — the installer. Gets Adobe apps onto your machine without hand-building a prefix. Collider runs it from its Mud Hut tab; it also runs standalone in a terminal.

Premiere Pro, Photoshop, and Lightroom Classic have been used for paid client work on this stack. See the [status board](/#status) for each application's current status.
