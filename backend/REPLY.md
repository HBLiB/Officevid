# Round 1 — Backend Reply

## Status: Done

## What was built

- **`app.py`** — Flask REST API with `/api/register` (201/409) and `/api/login` (200/401) endpoints, plus static file serving for `../frontend/` at `/`.
- **`requirements.txt`** — Flask, bcrypt, PyJWT (unpinned; no network available to verify exact versions).
- **`LLD.md`** — documents schema, API contracts, and design decisions.

## Decisions

- Passwords hashed with bcrypt (auto-salted).
- JWT tokens use HS256, 24h expiry, `sub` = user id. Secret from `SECRET_KEY` env var.
- SQLite DB auto-created on startup via `init_db()`.
- Both register and login return 400 if email/password missing from request body.
- Could not run live tests — no network access to install dependencies. Code is syntax-checked.

## Files changed

- `backend/app.py` (new)
- `backend/requirements.txt` (new)
- `backend/LLD.md` (new)
- `backend/REPLY.md` (new)
