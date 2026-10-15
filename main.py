from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Pytest and Postman Demo")

DB_NAME = "demo.db"


def initialize_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)


initialize_db()


class User(BaseModel):
    name: str
    email: str


@app.post("/users", status_code=201)
def create_user(user: User):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row

            cursor = conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (user.name, user.email)
            )

            row = conn.execute(
                "SELECT * FROM users WHERE id = ?",
                (cursor.lastrowid,)
            ).fetchone()

            return dict(row)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


@app.get("/users/{user_id}")
def get_user(user_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return dict(row)


@app.get("/users")
def get_users():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM users").fetchall()

    return [dict(row) for row in rows]