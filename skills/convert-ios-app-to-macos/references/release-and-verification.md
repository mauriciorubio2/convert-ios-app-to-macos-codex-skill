# Release And Verification

Use this reference before packaging, uploading, or reporting that a converted Mac app is ready.

## Local Build Verification

For Xcode apps, verify the project shape:

```sh
xcodebuild -list -project App.xcodeproj
xcodebuild build -project App.xcodeproj -scheme "Mac Scheme" -destination 'platform=macOS'
xcodebuild test -project App.xcodeproj -scheme "iOS Scheme" -destination 'platform=iOS Simulator,name=iPhone 17 Pro'
```

Prefer a project-local runner:

```sh
./script/build_and_run.sh --verify
```

The runner should kill an existing app process, build the Mac target, launch the app, and verify the process exists. Keep it outside app source.

## Target And Bundle Checks

Before release work, confirm:

- macOS target has the expected product bundle identifier.
- iOS and macOS target memberships are correct.
- Mac app icon and asset catalog exist.
- Mac entitlements cover sandbox, network, location, file access, or other product needs.
- Info.plist contains required purpose strings for platform APIs.
- Marketing version and build number are intentional for each platform.
- iOS version/build is unchanged if it is frozen.

## App Store Packaging

For Mac App Store distribution:

- Archive the macOS scheme with an explicit archive path.
- Export a `.pkg` with Mac App Store export options.
- Verify the package is signed and contains the expected bundle version, build, architectures, assets, and entitlements.
- Dry-run upload and metadata operations before live changes.
- Use authenticated Xcode upload fallback when API upload fails on Apple-side checksum or tool limitations, but only after the binary is locally verified.

For iOS regression confidence:

- Build or test iOS, but do not upload or mutate iOS release state unless the user asks.

## Subscriptions And Universal Purchase

For shared iOS/macOS products:

- Keep entitlement concepts consistent across platforms.
- Verify product IDs, offering/package mappings, pricing, trial policy, and platform availability before release.
- If using RevenueCat, verify project, app, public SDK key, products, entitlement, offerings/packages, store state, and observed SDK/customer data where possible.
- If using native StoreKit, keep RevenueCat wording honest: do not claim runtime RevenueCat analytics until the SDK actually records receipts.

## Live-State Gates

Before saying ready:

- Read back selected build and processing state.
- Read back version state and localization/review-detail IDs.
- Verify screenshots are complete, nonblank, and platform-appropriate.
- Verify subscription status, availability, and review screenshots when subscriptions exist.
- Record live IDs and verification output in release configs or handoff docs.

Before mutating App Store Connect:

- Run preflight checks.
- Run dry-run plans.
- Ask for explicit confirmation for upload, metadata apply, screenshot upload, pricing changes, or review submission if the relevant workflow requires it.

## Handoff

End with:

- Current branch and commit.
- Exact files changed.
- Verification commands and results.
- Live release state if checked.
- Known dirty files intentionally preserved.
- Next manual gate or next Codex task.
