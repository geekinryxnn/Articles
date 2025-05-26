import pytest
from lib.models.magazine import Magazine
from lib.database.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM magazines")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Test Mag', 'Test')")
    conn.commit()
    conn.close()

def test_magazine_creation(setup_db):
    mag = Magazine("New Mag", "New Cat")
    mag.save()
    assert mag.id is not None

def test_find_magazine_by_id(setup_db):
    mag = Magazine.find_by_id(1)
    assert mag.name == "Test Mag"
    assert mag.category == "Test"