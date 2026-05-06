# Frontend Low-Level Design — Login Page

## Overview

Single-page login/register UI built with vanilla HTML, CSS, and JavaScript (no frameworks).

## Files

| File | Purpose |
|------|---------|
| `index.html` | Semantic markup: centered card with email/password form, feedback area, and login/register toggle |
| `style.css` | Responsive centered card layout using flexbox; mobile-friendly with `max-width: 400px` |
| `app.js` | IIFE handling form submission and mode toggling between login and register |

## Design Decisions

1. **Single form, two modes** — Rather than two separate pages or forms, the login and register views share the same form and toggle between modes via a link. This keeps the UI simple and avoids duplication.
2. **`fetch` with JSON** — Posts `{ email, password }` to `/api/login` (expects `200`) or `/api/register` (expects `201`) per the API contract. Errors display the server's `error` field.
3. **No client-side routing** — Not needed for a single view; keeps complexity low.
4. **Accessible feedback** — The feedback paragraph uses `role="status"` so screen readers announce changes.
5. **No token storage yet** — On successful login the token is received but not persisted; storage strategy (cookie vs localStorage) will be decided with the backend team in a future round.
