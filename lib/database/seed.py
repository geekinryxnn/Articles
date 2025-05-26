from lib.database.connection import get_connection
from lib.models.author import Author  
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Clear existing data
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    
    # Seed authors
    authors = [
        Author("J.K. Rowling"),
        Author("Stephen King"),
        Author("Toni Morrison")
    ]
    for author in authors:
        author.save()
    
    # Seed magazines
    magazines = [
        Magazine("Fantasy Today", "Fiction"),
        Magazine("Horror Monthly", "Horror"),
        Magazine("Literary Review", "Literature")
    ]
    for magazine in magazines:
        magazine.save()
    
    # Seed articles
    articles = [
        Article("Harry Potter and the Sorcerer's Stone", 1, 1),
        Article("The Shining", 2, 2),
        Article("Beloved", 3, 3),
        Article("Fantastic Beasts", 1, 1)
    ]
    for article in articles:
        article.save()
    
    conn.commit()
    conn.close()