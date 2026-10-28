---
title: Premiere Pro on Linux
status: feature
sub: What works in Adobe Premiere Pro on Linux with Neutron, and how to get it running.
description: Run Adobe Premiere Pro 2026 and 2025 on Linux with Neutron: GPU rendering, NVENC export, Dynamic Link, panels and VST3 audio plugins. Free and open source.
---

Neutron runs Adobe Premiere Pro on Linux: Premiere Pro 2026 and 2025, installed straight from Adobe and signed in with your own Adobe account. It's in beta, stable for editing and delivery, and it has been used for paid client work.

## What works

- **GPU (Mercury) rendering and timeline playback**: through CUDA on NVIDIA, and through OpenCL on AMD (Premiere Pro 2026).
- **Hardware NVENC export** that muxes natively into a valid MP4.
- **Dynamic Link** with After Effects, in both directions.
- **Panels**: Captioneer and other third-party panels are in daily use.
- **VST3 audio plugins**: tested with FabFilter Pro-Q 4 and plugdata. Load a new one with Premiere's Audio Plug-in Manager: see [Installing plugins](/wiki/start/basics/plugins/).
- **GPUs**: NVIDIA, AMD and Intel. On AMD, Premiere Pro 2026 uses the GPU through AMD's ROCm OpenCL. On Intel, it runs very well on Iris Xe graphics with Intel's OpenCL runtime.

## Get it running

[Install Collider](/wiki/start/basics/install-collider/), install Premiere Pro from its Mud Hut tab, then see [Running your first app](/wiki/start/basics/first-app/). Current problems, such as a 2026 thumbnail that can show "Media pending" after a project is reopened, are listed under [Known issues](/wiki/start/help/known-issues/).
