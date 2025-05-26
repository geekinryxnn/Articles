# scripts/setup_db.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    with open('lib/db/schema.sql') as f:
        schema = f.read()
    
    cursor.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    print("Database tables created successfully!")