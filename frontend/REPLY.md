# Round 2 — Frontend Reply

## Status: Done

## What I changed

- **index.html** — Added an inline SVG logo (blue rounded square with white "H") and "H-Network" text above the form title.
- **style.css** — Added `.logo` and `.logo-text` styles to center the logo and visually balance it with the card layout.

## Decisions

1. Used an inline SVG rather than an external image file — no extra requests, scales cleanly.
2. Matched the logo background color to the existing button/accent color (`#4a6cf7`) for visual consistency.
3. Added `aria-label` on the logo container for accessibility.
