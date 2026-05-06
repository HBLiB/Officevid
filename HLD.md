# HLD — Officevid

## Overview

Officevid is a simple web application with a login page backed by a database for user authentication.

## Architecture

```
┌────────────┐       HTTP        ┌────────────┐       SQL        ┌────────────┐
│  Frontend  │  ──────────────►  │  Backend   │  ─────────────►  │     DB     │
│  (static)  │  ◄──────────────  │  (API)     │  ◄─────────────  │  (SQLite)  │
└────────────┘                   └────────────┘                   └────────────┘
```

## Components

### Frontend (`frontend/`)

- Single-page login form (HTML/CSS/JS)
- Sends credentials to backend API via `POST /api/login`
- Displays success/failure feedback to the user
- No framework — plain HTML + vanilla JS

### Backend (`backend/`)

- REST API server (Python / Flask)
- Endpoints:
  - `POST /api/login` — authenticate user (email + password)
  - `POST /api/register` — create new user
- Passwords stored hashed (bcrypt)
- Returns session token on successful login

### Database

- SQLite (file-based, no external service needed)
- Single `users` table:

  | Column | Type | Notes |
  |--------|------|-------|
  | id | INTEGER | PK, autoincrement |
  | email | TEXT | unique, not null |
  | password_hash | TEXT | bcrypt hash |
  | created_at | TIMESTAMP | default now |

## Contracts

| Route | Method | Request Body | Response |
|-------|--------|-------------|----------|
| `/api/login` | POST | `{ "email": "...", "password": "..." }` | `200 { "token": "..." }` or `401 { "error": "..." }` |
| `/api/register` | POST | `{ "email": "...", "password": "..." }` | `201 { "id": ... }` or `409 { "error": "..." }` |

## Directory Layout

```
/
├── HLD.md
├── frontend/          # owned by frontend team
│   ├── LLD.md
│   ├── index.html
│   ├── style.css
│   └── app.js
├── backend/           # owned by backend team
│   ├── LLD.md
│   ├── app.py
│   ├── requirements.txt
│   └── users.db       (generated at runtime)
└── instructions/
```

## Tech Choices

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Frontend | Vanilla HTML/JS | Simplicity; no build step |
| Backend | Python + Flask | Minimal boilerplate |
| DB | SQLite | Zero config, file-based |
| Auth | bcrypt + token | Industry standard hashing |

## Non-Goals (v1)

- No OAuth / social login
- No session management beyond token issuance
- No deployment infrastructure
- No password reset flow
