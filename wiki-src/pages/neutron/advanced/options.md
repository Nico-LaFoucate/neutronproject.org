---
title: Advanced options
status: guide
sub: Switches for testing and troubleshooting. Each one has a cost.
---

These are for testing and troubleshooting. The normal guides never need them, and each one can make things worse.

## Turn one fix off

`neutron launch <app> --without <fix>` launches with one of Neutron's shipped fixes turned off, for that launch only. `neutron gates` lists the fixes you can turn off. Use it to check whether a fix is behind a problem you're seeing.

**Risk:** with the fix off, the app can misbehave in exactly the way that fix exists to prevent.

## Launch on a different runtime

`neutron launch <app> --allow-restamp` launches even when the installed runtime isn't the one the prefix was set up with.

**Risk:** Wine updates the prefix and reverts Neutron's patched files in it, so apps can break until you run `neutron prefix provision <prefix>`. Use it only when you're deliberately moving a prefix to a new runtime; `neutron update` normally does that for you.

## Pick a runtime version

Set `NEUTRON_WINE_VERSION=<version>` to use a specific installed neutron-wine runtime instead of the newest one. The app menu entries pin their version the same way.

**Risk:** a prefix set up with a different runtime refuses to launch on it (see `--allow-restamp`).

## Launch on X11

X11 isn't supported. Setting `NEUTRON_ALLOW_X11=1` lets an app launch in an X11 session anyway.

**Risk:** many of Neutron's display and window fixes live in its Wayland driver, so they don't apply. It also switches the prefix's graphics driver to X11; a later Wayland launch switches it back. You're on your own: bug reports from X11 sessions aren't supported.
