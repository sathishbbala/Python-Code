from ui.app import UI
service = UI()

#service.add_expense(
#    employee=1,
#    category=2,
#    amount=1500,
#    date="2024-03-01"
#)

#service.modify_expense(
#    expense_id=3,
#    employee=1,
#    category=4,
#    amount=2200,
#    date="2024-03-02"
#)

service.delete_expense(expense_id=1788888)