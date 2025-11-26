from service.expense_service import ExpenseService

class UI:

    def __init__(self):
        self.repo = ExpenseService()

    def add_expense(self, employee, category, amount, date):
        self.repo.add_expense(employee, category, amount, date)

    def delete_expense(self, expense_id):
        self.repo.delete_expense(expense_id)

    def modify_expense(self, expense_id, employee, category, amount, date):
        self.repo.modify_expense(expense_id, employee, category, amount, date)
