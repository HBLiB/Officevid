import os
import sqlite3
import datetime

from flask import Flask, request, jsonify, send_from_directory
import bcrypt
import jwt

app = Flask(__name__, static_folder="../frontend", static_url_path="")

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "email and password required"}), 400

    email = data["email"]
    password = data["password"]

    pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    conn = get_db()
    try:
        cur = conn.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (email, pw_hash),
        )
        conn.commit()
        user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "email already registered"}), 409
    conn.close()
    return jsonify({"id": user_id}), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "email and password required"}), 400

    email = data["email"]
    password = data["password"]

    conn = get_db()
    row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "invalid credentials"}), 401

    if not bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8")):
        return jsonify({"error": "invalid credentials"}), 401

    token = jwt.encode(
        {
            "sub": row["id"],
            "email": row["email"],
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(hours=24),
        },
        SECRET_KEY,
        algorithm="HS256",
    )
    return jsonify({"token": token}), 200


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
