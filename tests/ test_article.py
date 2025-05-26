import pytest
from lib.models.article import Article
from lib.database.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM articles")
    cursor.execute("INSERT INTO authors (name) VALUES ('Test Author')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Test Mag', 'Test')")
    cursor.execute("""
        INSERT INTO articles (title, author_id, magazine_id)
        VALUES ('Test Article', 1, 1)
    """)
    conn.commit()
    conn.close()

def test_article_creation(setup_db):
    article = Article("New Article", 1, 1)
    article.save()
    assert article.id is not None

def test_find_article_by_id(setup_db):
    article = Article.find_by_id(1)
    assert article.title == "Test Article"