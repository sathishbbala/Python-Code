from faker import Faker
import csv, random
from datetime import datetime, timedelta

faker = Faker("en_IN") # setting US to get localized data
employees =[]
categories = ["Travel","Meals","Accommodation","Software","Hardware","Training","Taxi","Internet","Office Supplies","Team Event"]
employee=[]

for i in range(100):
    employees.append(faker.name())

field_names=["emp_name", "expense_category", "expense_amount", "expense_date"]
with open("data/expense_transactions.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(field_names)
    for i in range(10000):
        employee.append(random.choice(employees))
        employee.append(random.choice(categories))
        employee.append(format(random.uniform(500, 5000),".2f"))
        employee.append(datetime.now().date()- timedelta(days=random.randint(0,365)))
        writer.writerow(employee)
        employee=[]