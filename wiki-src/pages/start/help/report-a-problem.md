---
title: Report a problem
status: guide
sub: Where each kind of problem goes, and what to include.
---

Each part of Neutron has its own issue tracker on GitHub:

- **An Adobe app misbehaves** (it won't start, draws wrong, crashes, or a feature doesn't work): [Neutron issues](https://github.com/Nico-LaFoucate/Neutron/issues).
- **Collider itself** (its window, buttons or settings): [Collider issues](https://github.com/Nico-LaFoucate/Collider/issues).
- **Installing apps with Mud Hut**: [Mud Hut issues](https://github.com/Nico-LaFoucate/Mud-Hut/issues).
- **The neutron-wine runtime itself** (downloading or building it): [neutron-wine issues](https://github.com/Nico-LaFoucate/neutron-wine/issues).

Not sure which? Use Neutron's issues.

## What to include

- The app, and what happened.
- Your distro, desktop and GPU.
- The output of `neutron --version`.
- The output of `neutron doctor --prefix <prefix>`.
- The newest log from `~/.local/share/neutron/logs/`. Launches from Collider, the app menu or a file write one automatically.

## Questions

Ask in Neutron's [Discussions](https://github.com/Nico-LaFoucate/Neutron/discussions).

## Security problems

Don't open a public issue. Report it privately through GitHub's private vulnerability reporting: [Neutron's security advisory form](https://github.com/Nico-LaFoucate/Neutron/security/advisories/new). That one form covers all four repositories.

`contact@neutronproject.org` is for press and business, not support.
