---
title: What Neutron does
status: guide
sub: The engine, and the one rule that holds it together.
---

Neutron is the engine everything else calls. It bundles **Neutron-Wine** (an owned Wine fork), **DXVK** and **vkd3d-proton** (Direct3D → Vulkan), a **DirectComposition bridge**, and an **nvcuda wrapper** — plus every Adobe-specific fix, from locale-loader patches to display handling.

All of it is exposed through a single command-line interface. There is no GUI requirement: the `neutron` CLI owns prefixes, environment, registry, and Wine-binary selection, and everything above it (Collider, Mud&nbsp;Hut, your terminal) just calls down into it.

<div class="callout"><p class="k">The one rule</p><p>The launcher never touches compatibility. Every fix lives in the engine, so it reaches all three entry points at once — and the launcher stays replaceable.</p></div>
