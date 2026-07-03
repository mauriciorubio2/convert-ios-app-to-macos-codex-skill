# Conversion Standard

Use this reference when a future conversion should keep iOS and macOS separate enough for platform quality while sharing enough product code to avoid drift.

## Core Principle

The macOS app should be separate enough to behave like a real Mac product, but shared enough that product behavior does not drift.

Default structure:

- One source repo unless the user explicitly asks for a separate macOS repo.
- Shared product code in a central module or folder.
- Independent iOS and macOS targets, schemes, entrypoints, entitlements, signing, build numbers, screenshots, and release configs.
- Platform UI shells that can vary, with common feature semantics and services underneath.

For a separate macOS repo request, keep the same principles but make the sync mechanism explicit: shared package dependency, subtree, submodule, generated copy step, or documented manual sync checklist. Do not create an untracked clone with no update story.

## Proven Pattern

The expected conversion pattern moves common app code into shared sources and splits platform entrypoints:

- Shared model, service, StoreKit/subscription, content, weather, news, preferences, and reusable view logic.
- iOS entrypoint and mobile shell kept in the iOS platform folder.
- macOS entrypoint, entitlements, Info.plist, window sizing, and app icon kept in the macOS platform folder.
- A dedicated Mac scheme and target built the desktop app.
- Tests continued to cover shared product rules through the existing iOS test target.

This avoided two bad outcomes:

- A full duplicate Mac codebase that would drift.
- A direct phone UI on desktop that technically builds but feels wrong.

## App Store And Product Identity

When the Mac app is the same product as the iOS app, prefer the Apple universal-purchase shape:

- Same App Store app record where appropriate.
- Same bundle identifier when adding macOS as another platform of the same app record.
- Same subscription product family and entitlement concept.
- Separate platform builds and release tracks.

Use a different bundle identifier or App Store record only when the Mac app is intentionally a separate product, has distinct pricing/access, or the user asks for separation.

Always verify current Apple and subscription-provider rules before mutating live release state.

## Frozen iOS Rule

If iOS is under review, approved, or otherwise release-sensitive:

- Do not bump the iOS version or build number.
- Do not change the selected iOS build in App Store Connect.
- Do not modify iOS release metadata as a side effect of macOS work.
- Run iOS tests/builds only as non-mutating regression checks.

Mac can have its own build number and package so Apple accepts the new desktop platform without disturbing the mobile review path.

## Documentation To Leave Behind

Add or update:

- README architecture section.
- Platform sync document explaining shared versus platform-specific files.
- Mac release plan with exact build, archive, export, screenshot, upload, and manual submission gates.
- Handoff file with git state, verification, known dirty files, and next action.

Conversions become easier to continue when the repo itself explains how iOS and macOS stay in sync.
