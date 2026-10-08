---
title: What Collider is
status: guide
sub: The launcher, and why it deliberately knows nothing about fixes.
---

Collider is a desktop application that finds your installed apps, checks that a prefix is healthy, launches it, and supervises it until it exits. For anything compatibility-related it calls the [Neutron](/wiki/neutron/) CLI — it holds no fixes of its own.

That separation is the point: the launcher can be rewritten or replaced without touching a single compatibility fix, and every fix Neutron gains shows up in Collider for free. Licensed Apache&nbsp;2.0.
