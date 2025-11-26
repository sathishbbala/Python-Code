import sqlite3, csv
class WriteData:
    def writeempdata(self):
        employees=[]
        with open("database/seed_data/employees.csv", "r") as csv_file:
            # reader = csv.reader(csv_file) # will include headers 
            reader = csv.DictReader(csv_file) # excludes headers
            for row in reader:
                employees.append(row)
            
        conn = sqlite3.connect("database/expense_tracker.db")
        cursor = conn.cursor()
        for employee in employees:
            cursor.execute("INSERT INTO employees (name, job_title, salary, hire_date) VALUES (?,?,?,?)", (employee["name"], employee["job_title"], employee["salary"], employee["start_date"]))
        conn.commit()
        conn.close()

    def writecategorydata(self):
        categories=[]
        with open("database/seed_data/categories.csv", "r") as csv_file:
            reader = csv.reader(csv_file) # will include headers
            next(reader) # use this to skip the header
            for row in reader:
                categories.append(row)
        conn = sqlite3.connect("database/expense_tracker.db")
        cursor = conn.cursor()
        for category_name in categories:
            cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name)) 
        conn.commit()
        conn.close()
