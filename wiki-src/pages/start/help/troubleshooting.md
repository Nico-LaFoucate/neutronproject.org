---
title: Troubleshooting
status: guide
sub: First steps when something goes wrong.
---

## Start with the health check

Run `neutron doctor --prefix <prefix>`. It checks the things that can stop an app from launching or running, and says what to do about each. Collider shows the same checks for the prefix you're using. Before an app's first launch, a line may say it's pending until that first launch; that's normal.

## An app refuses to launch

- **"No Wayland session detected":** log in to a Wayland session. X11 isn't supported.
- **The runtime and the prefix don't match** (after a new runtime was installed): run `neutron update`, or `neutron prefix provision <prefix>` for one prefix.
- **Mud Hut says neutron-wine isn't installed:** run `neutron setup` first.

## A plugin won't activate, or keeps asking to be activated again

Some license servers block VPN addresses. Activate the plugin with your VPN off, or exclude the Adobe app from the VPN with split tunneling. The plugin's periodic online check needs the same.

## An extension panel is blank

If a panel that worked goes blank after the extension updates itself, run `neutron prefix provision <prefix>`, then restart the app. For other blank panels, see [Plugins and extensions](/wiki/neutron/features/plugins/).

## Still stuck

Check [Known issues](/wiki/start/help/known-issues/), then [report the problem](/wiki/start/help/report-a-problem/).
