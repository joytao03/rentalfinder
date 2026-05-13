import sqlite3
from datetime import datetime

DB_NAME = "rentals.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            price INTEGER,
            location TEXT,
            room_type TEXT,
            move_in_date TEXT,
            contact TEXT,
            raw_text TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_rental(rental: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO rentals (
            title,
            url,
            price,
            location,
            room_type,
            move_in_date,
            contact,
            raw_text,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        rental.get("title"),
        rental.get("url"),
        rental.get("price"),
        rental.get("location"),
        rental.get("room_type"),
        rental.get("move_in_date"),
        rental.get("contact"),
        rental.get("raw_text"),
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_all_rentals():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM rentals
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]