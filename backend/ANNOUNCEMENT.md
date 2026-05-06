# Round 1 — Backend

## Task

Build the authentication API and database for Officevid.

## Requirements

1. Create `app.py` — Flask REST API with:
   - `POST /api/register` — create user (email + password), hash password with bcrypt, return `201 { "id": ... }` or `409` on duplicate
   - `POST /api/login` — verify credentials, return `200 { "token": "..." }` or `401 { "error": "..." }`
   - Serve `frontend/` as static files at `/` (so the whole app runs from one server)
2. Create `requirements.txt` with dependencies (Flask, bcrypt, etc.)
3. SQLite database (`users.db`, auto-created on startup) with table:
   - `id` INTEGER PK autoincrement
   - `email` TEXT unique not null
   - `password_hash` TEXT not null
   - `created_at` TIMESTAMP default current
4. Create `LLD.md` documenting your design decisions

## Contracts

| Route | Method | Request Body | Response |
|-------|--------|-------------|----------|
| `/api/login` | POST | `{ "email": "...", "password": "..." }` | `200 { "token": "..." }` or `401 { "error": "..." }` |
| `/api/register` | POST | `{ "email": "...", "password": "..." }` | `201 { "id": ... }` or `409 { "error": "..." }` |

## Scope

Only touch files inside `backend/`. Use SQLite (no external DB service).
