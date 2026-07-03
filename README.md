# Convert iOS App to macOS Codex Skill

This repository contains a Codex skill for converting an existing iOS app into a macOS app using a shared-code, independent-platform standard: shared product code, independent platform targets, desktop-native Mac UI, separate release tracks, and real verification.

## Install

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mauriciorubio2/convert-ios-app-to-macos-codex-skill --path skills/convert-ios-app-to-macos
```

Restart Codex after installation so the skill is discovered.

## Use

Example prompts:

```text
Use $convert-ios-app-to-macos to add a Mac version of this iOS SwiftUI app while keeping iOS unchanged.
```

```text
Use $convert-ios-app-to-macos to convert this iOS app into a shared-code macOS app with a desktop-native sidebar and release checklist.
```

```text
Use $convert-ios-app-to-macos and preserve the iOS build that is already under App Store review.
```

## What It Covers

- Repo-first discovery and dirty-worktree protection.
- Shared code extraction for models, services, stores, subscriptions, and reusable SwiftUI views.
- Independent iOS/macOS targets, schemes, entrypoints, entitlements, icons, Info.plists, build numbers, and release configs.
- macOS UI adaptation with desktop navigation, toolbars, keyboard shortcuts, windows, settings, and screenshot handling.
- Build, launch, test, archive, package, dry-run, live-readback, and handoff expectations.

## Privacy And Safety

The skill is procedural guidance only. It does not include private app identifiers, credentials, API keys, App Store Connect tokens, RevenueCat keys, screenshots, or customer data. Future users should keep release credentials in their own secure local environment and should not publish app-specific secrets in skill references or public issues.

## Development

Run these checks from the repo root:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/convert-ios-app-to-macos
python3 ~/.codex/skills/open-source-codex-skill-creator/scripts/validate_public_skill_repo.py .
python3 tests/test_skill_repo.py
git diff --check
```

## Contributing

Focused improvements are welcome. Please include a short summary of what changed, why it helps future iOS-to-macOS conversions, and any validation you ran.

## License

MIT
