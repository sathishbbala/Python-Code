import csv

employee_high_salary=[] # list with dictionary as each element

with open("data/employees.csv") as csv_file:
    # reader = csv.reader(csv_file) # will include headers 
    reader = csv.DictReader(csv_file) # excludes headers
    for row in reader:
        if int(row["salary"]) > 80000:
            employee_high_salary.append(row)

with open("data/employees_higher_salaries.csv", "w", newline="") as csv_file_2:
    writer = csv.DictWriter(csv_file_2, fieldnames=employee_high_salary[0].keys())
    writer.writeheader()
    writer.writerows(employee_high_salary)

print(employee_high_salary[0].keys())
print(employee_high_salary)