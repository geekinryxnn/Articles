from lib.database.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id))
        else:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    @classmethod
    def find_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['name'], row['category'], row['id']) for row in rows]

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['title'], row['author_id'], row['magazine_id'], row['id']) for row in rows]

    def contributors(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row['name'], row['id']) for row in rows]