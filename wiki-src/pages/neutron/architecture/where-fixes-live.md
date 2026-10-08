---
title: Where the fixes live
status: guide
sub: Neither Wine nor Adobe is broken — the defect is in the seam.
---

Neither Wine nor Adobe is broken on its own. The defects live in the **seam** between two healthy systems, and that seam is where Neutron patches. The stack is four tiers:

### Cockpit — entry points

The Collider GUI, the Mud&nbsp;Hut installer, or a plain terminal. Nothing here owns compatibility logic.

### Contract — the neutron CLI

A hard boundary. Calls travel down; status comes back as JSON. Above the line: convenience. Below the line: compatibility.

### Engine — Neutron

Owns prefixes, environment, registry, Wine-binary selection, and every compat fix.

### Runtime

Neutron-Wine hosts the Adobe application alongside DXVK, vkd3d-proton, the dcomp bridge, and the nvcuda wrapper.

### Substrate

Vulkan, your GPU, and the Linux kernel.

Because the launcher and installer sit above the contract line, they can be rewritten or removed without touching a single fix — and every fix Neutron gains reaches all three entry points at once.
