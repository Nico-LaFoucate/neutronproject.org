---
title: How runtimes are versioned
status: guide
sub: Proton-style: the repo is the recipe, releases are prebuilt trees.
---

Neutron ships Wine the Proton-GE way. The **neutron-wine** repo is the *recipe* — a patch set plus a pinned upstream Wine base — and each release is a **prebuilt, self-contained Wine tree** attached to a versioned release. You never build Wine; the engine downloads and verifies a tarball.

Versions look like `11.10-12`: the `11.10` tracks the upstream Wine base, and the `-12` is the Neutron revision — it bumps whenever the patch set changes. Because every runtime is reproducible from the tracked patch set, a fix is never a hand-swapped binary; it is a patch that rebuilds cleanly into the next release.

An app is pinned to the runtime it was last booted against — launching against a different one triggers a prefix update, so the engine keeps that mapping deliberate.
