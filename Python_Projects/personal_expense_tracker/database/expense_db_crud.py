import sqlite3

class ExpenseRepository:

    def __init__(self, db_path="database/expense_tracker.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def add_expense(self, employee_id, category_id, amount, date):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses (employee_id, category_id, expense_amount, expense_date)
            VALUES (?, ?, ?, ?)
            """,
            (employee_id, category_id, amount, date)
        )
        conn.commit()
        conn.close()

    def delete_expense(self, expense_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM expenses WHERE expense_id = ?",
            (expense_id,)
        )
        conn.commit()
        conn.close()

    def update_expense(self, expense_id, employee_id, category_id, amount, date):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE expenses 
            SET employee_id = ?, category_id = ?, expense_amount = ?, expense_date = ?
            WHERE expense_id = ?
            """,
            (employee_id, category_id, amount, date, expense_id)
        )
        conn.commit()
        conn.close()