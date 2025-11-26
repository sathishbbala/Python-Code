import sqlite3, random
from datetime import datetime, timedelta

class GenerateTransactions():

    def generate_transactions(self, num_transactions):
        conn = sqlite3.connect("database/expense_tracker.db")
        cursor = conn.cursor()
        for transaction_number in range(num_transactions):
            cursor.execute("SELECT emp_id FROM employees ORDER BY RANDOM() LIMIT 1")
            random_emp_id = cursor.fetchone()[0]
            cursor.execute("SELECT category_id FROM categories ORDER BY RANDOM() LIMIT 1")
            random_category_id = cursor.fetchone()[0]
            amount = format(random.uniform(250, 3000), ".2f")
            days_back = random.randint(0, 30) # random number of days between 0 and 90
            random_date = datetime.now() - timedelta(days=days_back)
            cursor.execute("INSERT INTO expenses (employee_id, category_id, expense_amount, expense_date) VALUES (?, ?, ?, ?)", (random_emp_id, random_category_id, amount, random_date))
        conn.commit()
        conn.close()
        print(f"Finished {num_transactions} Transactions")
