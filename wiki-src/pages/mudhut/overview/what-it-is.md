---
title: What Mud Hut is
status: guide
sub: Installs Adobe apps without hand-building a prefix.
---

Mud Hut is a command-line installer that gets Adobe applications onto your machine without hand-building a Wine prefix. [Collider](/wiki/collider/) runs it from its Mud Hut tab, and it runs standalone for anyone who prefers a terminal.

Under the hood it leans on Neutron's `prefix provision` — the single, reproducible recipe for making a prefix Adobe-ready — so an install done through Mud Hut and one done by hand end up in the same known-good state.
