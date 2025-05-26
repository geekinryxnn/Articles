# scripts/setup_db.py
import sqlite3
from lib.database.connection import get_connection

def setup_database():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database setup complete")

if __name__ == "__main__":
    setup_database()