---
title: What Mud Hut is
status: guide
sub: One-click Adobe install, no manual prefix.
---

Mud Hut is a command-line installer that gets Adobe applications onto your machine without hand-building a Wine prefix. It ships inside [Collider](/wiki/collider/) as one-click install, and runs standalone for anyone who prefers a terminal.

Under the hood it leans on Neutron's `prefix provision` — the single, reproducible recipe for making a prefix Adobe-ready — so an install done through Mud Hut and one done by hand end up in the same known-good state.
