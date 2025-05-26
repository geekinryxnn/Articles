import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.database.seed import seed_database
from .models import Author
from .models.magazine import Magazine
from .models import Article

def display_data():
    print("\n=== Current Database State ===")
    
    print("\nAuthors:")
    for author in Author.find_all():
        print(f"- {author.name} (ID: {author.id})")
    
    print("\nMagazines:")
    for magazine in Magazine.find_all():
        print(f"- {magazine.name} ({magazine.category}, ID: {magazine.id})")
    
    print("\nArticles:")
    for article in Article.find_all():
        print(f"- '{article.title}' by Author ID {article.author_id} in Magazine ID {article.magazine_id}")

if __name__ == '__main__':
    seed_database()
    display_data()