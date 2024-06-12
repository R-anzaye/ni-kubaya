import sqlite3

class Comment:
    def __init__(self, id_, maintenance_id, comment):
        self.id = id_
        self.maintenance_id = maintenance_id
        self.comment = comment

    def save(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO comment (maintenance_id, comment)
            VALUES (?,?)
        """, (self.maintenance_id, self.comment))
        self.id = cursor.lastrowid  # Get the last inserted id
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, maintenance_id, comment FROM comment")
        comments = cursor.fetchall()
        conn.close()
        return comments

    @classmethod
    def find_by_id(cls, id_):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, maintenance_id, comment FROM comment WHERE id=?", (id_,))
        result = cursor.fetchone()
        conn.close()
        if result:
            id_, maintenance_id, comment = result
            return cls(id_, maintenance_id, comment)
        return None

    def delete(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM comment WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    def update(self, new_comment):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE comment SET comment=?
            WHERE id=?
        """, (new_comment, self.id))
        conn.commit()
        conn.close()