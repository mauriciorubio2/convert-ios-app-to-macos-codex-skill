---
name: convert-ios-app-to-macos
description: "Convert an existing iOS Swift or SwiftUI app into a desktop-native macOS app using a shared-code, independent-platform standard: shared product code, independent iOS and macOS targets or repos where requested, macOS-specific entrypoints, UI, signing, screenshots, release configs, and verification. Use when asked to port, convert, add a Mac version, create a companion macOS app, preserve iOS while building macOS, keep iOS and macOS in sync, or optimize an iOS app for macOS."
---

# Convert iOS App To macOS

## Overview

Use this skill to turn an iOS app into a macOS app without making a stale clone. Default to the shared-code, independent-platform standard: shared model/service/product behavior, separate platform shells, separate schemes/build tracks, and Mac UI that feels native to desktop.

If the `Build macOS Apps` plugin is available, use it while working: `swiftui-patterns` for scenes/layouts, `build-run-debug` for build/run automation, and `appkit-interop` or `window-management` only when SwiftUI cannot express the desktop behavior cleanly.

## Workflow

### 1. Anchor The Repo

- Locate the iOS repo and read repo-local instructions: `AGENTS.md`, `CODEX_HANDOFF.md`, README, release docs, and the current git state.
- Run `git status --short --branch` and `git diff --stat` before editing.
- Preserve unrelated dirty files, especially release artifacts, schemes, screenshots, and promo-code folders.
- Identify the active Xcode project/workspace, iOS scheme, tests, signing settings, bundle ID, current App Store version/build, and whether iOS is under review.

### 2. Choose The Sharing Model

- Default to one source repo with shared product code and independent platform targets.
- If the user explicitly asks for a separate macOS repo, create a sibling repo only after defining how shared code will be copied, packaged, vendored, or synchronized. Do not silently fork a stale one-off clone.
- Put common models, services, stores, business rules, networking, subscriptions, and reusable page components in a shared module or `Shared/` folder.
- Keep platform app entrypoints, scenes, windows, entitlements, Info.plists, app icons, platform settings, and release files platform-specific.

Read `references/conversion-standard.md` when you need the conversion pattern in more detail.

### 3. Build The Mac Target

- Add a separate macOS target, scheme, entrypoint, entitlements, Info.plist, and Mac app icon.
- Use the same bundle ID and App Store app record only when the app should be an Apple universal purchase or added Mac platform for the same product. Use a separate identifier only when the Mac app is intentionally a different product.
- Give macOS its own build number, signing settings, archive path, screenshots, and release config. Do not bump iOS just to ship Mac.
- Add or update `script/build_and_run.sh` and `.codex/environments/environment.toml` when this is a macOS app repo so Codex can build and launch through a stable path.

### 4. Make It Desktop-Native

- Do not present a stretched phone UI as the Mac app.
- Prefer desktop shells: sidebar/detail or `NavigationSplitView`, toolbar actions, keyboard shortcuts, clickable controls, settings scenes, command menus, pointer-friendly hit targets, and sensible default/minimum window sizes.
- Preserve the iOS flow unless the user asks to change it. Use `#if os(macOS)` or separate platform files to vary Mac layout while reusing product behavior.
- Where the Mac should vary slightly, vary shell, navigation, windowing, density, controls, screenshots, and platform services. Keep core feature semantics and subscription access consistent.

Read `references/desktop-adaptation.md` before making substantial UI changes.

### 5. Verify Both Platforms

- Build and launch macOS through the project script or `xcodebuild`.
- Run iOS tests or at least an iOS build as a non-mutating guardrail.
- Verify target membership, bundle identifiers, Info.plist purpose strings, entitlements, assets, app icons, signing, and universal-purchase/subscription assumptions.
- Generate or refresh Mac screenshots using deterministic app-rendered paths when screen capture is brittle.
- For release work, dry-run App Store Connect operations first and require explicit confirmation before live upload, metadata mutation, or review submission.

Read `references/release-and-verification.md` before packaging, uploading, or changing release metadata.

### 6. Leave A Clean Handoff

- Update `CODEX_HANDOFF.md`, README, and architecture/release docs when code or product state changes.
- Commit and push scoped changes when the repo/product state changed, unless the user explicitly says not to.
- Keep unrelated local changes unstaged and call them out in the final response.
- Summarize the exact verification commands and the next manual gate, especially if App Store review submission is intentionally not performed.

## Guardrails

- If iOS is already under review or approved, freeze the iOS build/version and release state unless the user explicitly asks for a new iOS release.
- Do not duplicate app logic between platforms. Extract it into shared code first.
- Do not hide Mac-only behavior inside generic shared views when a platform file or `#if os(macOS)` block makes the boundary clearer.
- Do not claim RevenueCat, App Store Connect, signing, screenshots, or uploaded builds are ready without live readback or local verification.
- Do not create a public release, upload, or submit for review without the required explicit confirmation from the relevant release workflow.

## References

- `references/conversion-standard.md`: shared-code architecture, repo, and release principles.
- `references/desktop-adaptation.md`: macOS UI, scene, window, and screenshot adaptation checklist.
- `references/release-and-verification.md`: build, test, App Store, subscription, and handoff verification.
