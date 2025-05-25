import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

@pytest.fixture
def db_setup():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()

def test_author_save(db_setup):
    author = Author("J.K. Rowling")
    author.save()
    assert author.id is not None