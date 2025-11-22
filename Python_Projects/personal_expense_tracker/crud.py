import sqlite3

class ExpenseTransactions:
    def AddExpense(self, employee, category, expense_amount, expense_date):
        self.employee = employee
        self.category = category
        self.expense_amount = expense_amount
        self.expense_date = expense_date

        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (employee_id, category_id, expense_amount, expense_date) VALUES (?,?,?,?)", (self.employee, self.category, self.expense_amount, self.expense_date))
        conn.commit()
        conn.close()

    def DeleteExpense(self,expense_id):
        self.expense_id = expense_id
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (self.expense_id,))
        conn.commit()
        conn.close()

    
    def ModifyExpense(self, expense_id, employee, category, expense_amount, expense_date):
        self.expense_id = expense_id
        self.employee = employee
        self.category = category
        self.expense_amount = expense_amount
        self.expense_date = expense_date
        conn = sqlite3.connect("expense_tracker.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE expenses SET employee_id = ?, category_id = ?, expense_amount = ?, expense_date = ? WHERE expense_id = ?", (self.employee, self.category, self.expense_amount, self.expense_date, self.expense_id))
        conn.commit()
        conn.close()

    
