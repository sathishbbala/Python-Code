import sqlite3

class ResetDatabase():
    def deleteallsqldata(self):
            conn = sqlite3.connect("database/expense_tracker.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses")
            cursor.execute("DELETE FROM categories")
            cursor.execute("DELETE FROM employees")
            conn.commit()
            conn.close()