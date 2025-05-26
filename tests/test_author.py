import sqlite3

def get_connection():
    # Adjust the database path as needed
    return sqlite3.connect('database.db')

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create articles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            content TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        )
    ''')
    
    # Create magazines table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT
        )
    ''')
    
    # Create authors table (if needed for your application)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Ensure tables exist before clearing data
    create_tables()
    
    # Clear existing data
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM authors")
    
    # Insert seed data (example)
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Doe",))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id, content) VALUES (?, ?, ?, ?)",
                  ("Tech Trends", 1, 1, "Article content here"))
    
    conn.commit()
    conn.close()

def test_example():
    assert 1 + 1 == 2