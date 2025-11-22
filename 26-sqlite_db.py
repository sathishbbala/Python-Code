import sqlite3, csv, random
from datetime import datetime, timedelta

def generate_data():
    employees=[] # List with dictionary as each element
    categories = ["Travel","Meals","Accommodation","Software","Hardware","Training","Taxi","Internet","Office Supplies","Team Event"]

    with open("data/employees.csv") as csv_file:
        # reader = csv.reader(csv_file) # will include headers 
        reader = csv.DictReader(csv_file) # excludes headers
        for row in reader:
            employees.append(row)

    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, job_title TEXT, salary INTEGER, hire_date DATE)
                """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (category_id INTEGER PRIMARY KEY AUTOINCREMENT, category_name TEXT) 
                """)
    for employee in employees:
        cursor.execute("INSERT INTO employees (name, job_title, salary, hire_date) VALUES (?,?,?,?)", (employee["name"], employee["job_title"], employee["salary"], employee["start_date"]))
    for category_name in categories:
        cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name,)) # additional comma is needed to avoid incorrect bindings error
        # a tuple with one value is passed to avoid the error
    conn.commit()
    conn.close()

def generate_transactions(num_transactions):
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (expense_id INTEGER PRIMARY KEY AUTOINCREMENT, employee_id INTEGER, category_id INTEGER, expense_amount REAL, expense_date TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY(employee_id) REFERENCES employees(id) ON DELETE CASCADE ON UPDATE CASCADE)
                    """)
    for transaction_number in range(num_transactions):
        cursor.execute("SELECT emp_id FROM employees ORDER BY RANDOM() LIMIT 1")
        random_emp_id = cursor.fetchone()[0]
        cursor.execute("SELECT category_id FROM categories ORDER BY RANDOM() LIMIT 1")
        random_category_id = cursor.fetchone()[0]
        amount = format(random.uniform(250, 3000), ".2f")
        days_back = random.randint(0, 30) # random number of days between 0 and 30
        random_date = datetime.now() - timedelta(days=days_back)
        cursor.execute("INSERT INTO expenses (employee_id, category_id, expense_amount, expense_date) VALUES (?, ?, ?, ?)", (random_emp_id, random_category_id, amount, random_date))
        print(f"Finished Transaction number {transaction_number}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    generate_data
    generate_transactions(1000)