import sqlite3
import csv
class WriteData:
    def WriteEmpData(self):
        employees=[]
        with open("employees.csv", "r") as csv_file:
            # reader = csv.reader(csv_file) # will include headers 
            reader = csv.DictReader(csv_file) # excludes headers
            for row in reader:
                employees.append(row)
            
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        for employee in employees:
            cursor.execute("INSERT INTO employees (name, job_title, salary, hire_date) VALUES (?,?,?,?)", (employee["name"], employee["job_title"], employee["salary"], employee["start_date"]))
        conn.commit()
        conn.close()

    def WriteCategoryData(self):
        categories=[]
        with open("categories.csv", "r") as csv_file:
            reader = csv.reader(csv_file) # will include headers
            next(reader) # use this to skip the header
            for row in reader:
                categories.append(row)
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        for category_name in categories:
            cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name)) 
        conn.commit()
        conn.close()

    def DeleteAllSQLData(self):
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses")
        cursor.execute("DELETE FROM categories")
        cursor.execute("DELETE FROM employees")
        conn.commit()
        conn.close()
