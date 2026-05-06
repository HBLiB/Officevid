# Backend Low-Level Design — Authentication API

## Overview

Flask REST API providing user registration and login with JWT-based authentication, backed by SQLite.

## Design Decisions

- **Flask** — lightweight, fits a single-file API well.
- **bcrypt** — industry-standard password hashing with built-in salting.
- **PyJWT** — generates HS256 tokens with 24-hour expiry; `sub` carries the user id.
- **SQLite** — zero-config, file-based; `users.db` is auto-created on first run via `init_db()`.
- **Static file serving** — Flask serves `../frontend/` at `/` so the whole app runs from one process.
- **Secret key** — read from `SECRET_KEY` env var, falls back to a dev default.

## Database Schema

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| email | TEXT | UNIQUE NOT NULL |
| password_hash | TEXT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## API Contracts

| Route | Method | Success | Error |
|-------|--------|---------|-------|
| `/api/register` | POST | `201 { "id": <int> }` | `409 { "error": "..." }` / `400` |
| `/api/login` | POST | `200 { "token": "..." }` | `401 { "error": "..." }` / `400` |
