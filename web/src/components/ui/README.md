<!--
  NOTICE

  The components in this directory (and the files listed below) are copied from
  1code by 21st.dev — https://github.com/21st-dev/1code — licensed under the
  Apache License, Version 2.0. Copyright 21st.dev. See reference/1code/LICENSE.

  "Verbatim" below means byte-identical to the 1code source apart from import
  paths (1code's `../../lib/utils` etc. resolve the same way here because this
  tree mirrors `src/renderer/`). "Adapted" files keep 1code's class names and
  structure but had Electron / tRPC / jotai / streamdown wiring removed or
  replaced with Scout's store.
-->

# UI kit — copied from 1code (Apache-2.0)

Source: `reference/1code/src/renderer/` at the commit vendored in this repo.

## Verbatim (`web/src/components/ui/`)

accordion, alert-dialog, badge, button-group, button, canvas-icons, checkbox,
collapsible, command, context-menu, dialog, dropdown-menu, error-boundary,
hover-card, icons, input, kbd, label, logo, popover, progress, prompt-input,
search-combobox, select, skeleton, split-button, switch, tabs, text-shimmer,
textarea, tooltip, typewriter-text.

Also verbatim:

- `web/src/lib/overlay-styles.ts` (shared classes for popover/select/command/menus)
- `web/src/lib/utils/format-time-ago.ts`
- `web/src/hooks/use-overflow-detection.ts`
- `web/src/styles/agents-styles.css`
- `web/src/features/chat/agent-message-usage.tsx` (import paths only)
- `web/tailwind.config.js` `theme.extend` (colors, borderRadius, screens), `darkMode`, plugins;
  `content` globs changed for Vite
- `web/postcss.config.js`

## Dropped (hard dependency on Electron / tRPC / jotai)

- `network-status.tsx` — jotai atom + tRPC query
- `resizable-sidebar.tsx`, `resizable-bottom-panel.tsx` — take a jotai `WritableAtom` as a prop
- `project-icon.tsx` — `lib/hooks/use-project-icon` (tRPC)

## Adapted

- `web/src/styles/globals.css` — identical minus the `@source "…streamdown…"` line
- `web/src/lib/utils.ts` — `cn()` verbatim; the `isMac` re-export from `utils/platform.ts`
  (which read `window.desktopApi`) replaced with a `navigator`-based check
- `web/src/features/layout/agents-layout.tsx` — shell structure and classes; atoms, hotkey
  manager, login modals, update banner, Windows title bar removed; sidebar width is local state
- `web/src/features/sidebar/agents-sidebar.tsx` — header row, search + "New" button,
  nav-link buttons, list rows with `TypewriterText`, footer; workspace/git/multi-select removed
- `web/src/features/chat/agent-user-message-bubble.tsx` — bubble + overflow fade + full-message
  dialog; image attachments, mentions and search highlighting removed
- `web/src/features/chat/agent-tool-call.tsx` — header row from `agent-tool-call.tsx` plus the
  collapsible pattern from `agent-web-search-collapsible.tsx`; body is a Scout card
- `web/src/features/chat/agent-thinking-tool.tsx` — header row only (Scout's `thinking` event is a
  one-line status)
- `web/src/features/chat/markdown.tsx` — `prose` class stack from `chat-markdown-renderer.tsx`,
  rendered with react-markdown instead of Streamdown + Shiki
- `web/src/features/chat/chat-input.tsx` — container classes from `chat-input-area.tsx` around the
  verbatim `prompt-input.tsx`
