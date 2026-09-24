# UMOD releases
Approved mission downloads and player-facing mod release notes for Universal Mod.

[Website](https://umod.rocks) · [Downloads](https://umod.rocks/downloads) · [Discord](https://discord.gg/TM89VN7Y7P)

Development repositories are private. The automatic Source code archives on GitHub releases contain this distribution repository, not the mission or mod. Download the named mission ZIP asset. Install finished mods through the Steam Workshop link in their release notes.

## Release format for maintainers
| Product | Stable tag | Required public file or link |
| --- | --- | --- |
| Universal Spawner | `universal-spawner/v1.0.0` | `UniversalSpawner.zip` |
| Universal Battle Tester | `universal-battle-tester/v1.0.0` | `UniversalBattleTester.Malden.zip` |
| Universal Signal Device | `universal-signal-device/v1.0.0` | Exact Steam Workshop line below |
| Universal Arsenal | `universal-arsenal/v1.0.0` | Exact Steam Workshop line below |

Replace 1.0.0 with the approved version. Create a draft first. Drafts, prereleases, tags with prerelease suffixes, unknown products, incomplete mission uploads and mods without a valid Steam link are excluded by the website.

For mods, include one standalone line:

```
Steam Workshop: https://steamcommunity.com/sharedfiles/filedetails/?id=ACTUAL_WORKSHOP_ID
```

Replace ACTUAL_WORKSHOP_ID with the verified numeric ID. Do not use an invented ID. This repository does not upload to Steam.

For missions, attach the exact expected ZIP filename. Put credits and required dependencies in the release notes. Publish only after the exact attached file has passed its relevant in-game check. Use `scripts/check_mission_zip.py` locally to check ZIP paths and basic packaging before uploading; it does not perform an Arma test.

Publishing a stable release makes it eligible for the website automatically. A source commit or merge alone does not publish anything. The website checks public releases approximately five minutes after the last successful fetch when visited. It presents recent versions and links to this complete archive.

## Release notes
Use `RELEASE_TEMPLATE.md`. Public notes explain what players need to know; the exact private source commit, internal bug discussion and test evidence belong in the private product repository.
