---
title: Choosing a display scale
status: guide
sub: Use a Windows scale step: 100, 125, 150, 175, 200, 225, 250 or 300%.
---

Neutron follows your desktop's display scale. Set it to one of the steps Windows offers: **100, 125, 150, 175, 200, 225, 250 or 300%**. Adobe's apps lay out their interface exactly only at those steps.

At other scales (170%, for example), parts of the interface land slightly off. In Premiere Pro, the marked in/out range on the timeline ruler drifts to the right of the selection. This comes from inside the app, not from Neutron; Windows users never see it because Windows only offers these steps.

To check, run `neutron display`. It shows the scale Neutron will use and warns when it isn't a Windows step.

In Collider, leave **Display scale** on **Auto (match desktop)**. Best results: set the same scale in your desktop's display settings. Picking a different scale in Collider doesn't fix it: your desktop then resizes the window, and it looks blurry.

## Not every desktop offers every step

- **GNOME 49 and newer** can't do 175% on 4K, 1440p or 1080p screens.
- **Hyprland** can't do 175% on 4K, 1440p or 1080p screens, or 150% on 1440p.

On those screens, pick another Windows step.
