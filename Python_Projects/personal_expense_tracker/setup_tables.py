import sqlite3

# create employees, categories and expenses tables
class CreateSQLTables:
    def CreateTables(self):
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, job_title TEXT, salary INTEGER, hire_date DATE)
                    """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (category_id INTEGER PRIMARY KEY AUTOINCREMENT, category_name TEXT) 
                    """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, employee_id INTEGER, category_id INTEGER, expense_amount REAL, expense_date TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE, 
        FOREIGN KEY(employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE)
                    """)
        conn.commit()
        conn.close()


