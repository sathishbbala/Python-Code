from database.expense_db_crud import ExpenseRepository

class ExpenseService:

    def __init__(self):
        self.repo = ExpenseRepository()

    def add_expense(self, employee, category, amount, date):
        # Add business validations here
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self.repo.add_expense(employee, category, amount, date)

    def delete_expense(self, expense_id):
        # Can check if expense exists before deleting
        self.repo.delete_expense(expense_id)

    def modify_expense(self, expense_id, employee, category, amount, date):
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        self.repo.update_expense(expense_id, employee, category, amount, date)