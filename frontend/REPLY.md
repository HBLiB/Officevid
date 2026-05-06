# Round 1 — Frontend Reply

## Status: Done

## What I built

- **index.html** — Login/register form with email + password fields, submit button, feedback area, and toggle link.
- **style.css** — Responsive centered card layout (flexbox, max-width 400px), clean styling with focus states.
- **app.js** — IIFE that handles form submission via `fetch` POST to `/api/login` or `/api/register`, displays success/error feedback, and toggles between login and register modes.
- **LLD.md** — Documents file responsibilities and design decisions.

## Decisions

1. Single form with mode toggle (login ↔ register) instead of separate pages.
2. Token received on login but not stored yet — storage strategy deferred to a future round.
3. Accessible feedback via `role="status"` on the message element.
