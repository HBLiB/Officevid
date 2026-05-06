# Round 1 — Frontend

## Task

Build the login page for Officevid.

## Requirements

1. Create `index.html` with a login form (email + password fields, submit button)
2. Create `style.css` — clean, centered login card, responsive
3. Create `app.js`:
   - On submit, `POST` to `/api/login` with `{ "email": "...", "password": "..." }`
   - Display success or error feedback to the user
   - Include a "Register" link/toggle that `POST`s to `/api/register` with the same payload
4. Create `LLD.md` documenting your design decisions

## Contracts

| Route | Method | Request Body | Response |
|-------|--------|-------------|----------|
| `/api/login` | POST | `{ "email": "...", "password": "..." }` | `200 { "token": "..." }` or `401 { "error": "..." }` |
| `/api/register` | POST | `{ "email": "...", "password": "..." }` | `201 { "id": ... }` or `409 { "error": "..." }` |

## Scope

Only touch files inside `frontend/`. No frameworks — vanilla HTML/CSS/JS.
