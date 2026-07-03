# Desktop Adaptation Checklist

Use this reference before changing a converted app's macOS UI.

## Do Not Ship A Large Phone Screen

The Mac version should respect desktop input and layout:

- Pointer and keyboard first, touch gestures optional or secondary.
- Explicit navigation instead of swipe-only flows.
- Stable window structure instead of deep push stacks where a sidebar/detail view fits.
- Toolbar, command menu, and keyboard shortcut exposure for common actions.
- Settings as a macOS settings scene or native-feeling surface, not just another mobile page.

## Mac Shell Patterns

Prefer one of these shapes:

- Sidebar/detail for dashboard, browsing, collection, or multi-page apps.
- Editor/detail with optional inspector for content creation or configuration.
- Single-window utility layout for small focused tools.
- Document window or multiwindow model when the product is document-based.
- Menu bar extra only when the product is naturally glanceable or background-first.

Keep the product's shared content views reusable, but wrap them in a Mac-specific shell when needed.

## Platform Differences That Are Good

It is acceptable and often necessary for macOS to vary in:

- Navigation controls and sidebar density.
- Toolbar placement and keyboard shortcuts.
- Window default/minimum sizes.
- Pointer hover and focus states.
- App icon format and desktop screenshot framing.
- Entitlements and Info.plist purpose strings.
- Settings, menus, and command routing.
- Screenshot generation and release assets.

It is usually not acceptable for macOS to drift in:

- Subscription entitlement rules.
- Core feature availability.
- Business logic and calculations.
- Content parsing, cache, sync, and service behavior.
- App identity unless the product is intentionally separate.

## Shared SwiftUI Files

If a shared SwiftUI file contains both platforms:

- Keep platform forks small and named.
- Use `#if os(macOS)` for shell and control differences.
- Move large platform views into platform files if the shared file becomes hard to reason about.
- Avoid leaking macOS-only APIs into iOS compile paths.
- Avoid changing the iOS route while fixing desktop usability.

## Visual QA

Do more than compile:

- Launch the Mac app and verify the main window appears.
- Check that navigation is visible without hidden gestures.
- Confirm text and controls fit at reasonable Mac window sizes.
- Generate desktop screenshots at the expected App Store dimensions when preparing release assets.
- If screen capture permissions are brittle, prefer a deterministic debug renderer that uses real app views and seeded data.
