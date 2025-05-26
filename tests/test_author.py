import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.database.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Clear tables
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    
    # Insert test data
    cursor.execute("INSERT INTO authors (name) VALUES ('Test Author')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Test Mag', 'Test')")
    cursor.execute("""
        INSERT INTO articles (title, author_id, magazine_id)
        VALUES ('Test Article', 1, 1)
    """)
    
    conn.commit()
    conn.close()

def test_author_creation(setup_db):
    author = Author("New Author")
    author.save()
    assert author.id is not None

def test_find_author_by_id(setup_db):
    author = Author.find_by_id(1)
    assert author.name == "Test Author"

def test_author_articles(setup_db):
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) == 1
    assert isinstance(articles[0], Article)