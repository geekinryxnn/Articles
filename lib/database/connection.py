import sqlite3

def get_connection():
    """Return a database connection with row factory set"""
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    return conn