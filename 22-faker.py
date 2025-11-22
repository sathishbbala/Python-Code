from faker import Faker
from datetime import date
import csv

faker = Faker("en_US") # setting US to get localized data

#print(faker.name(), faker.email(), faker.address(), faker.phone_number())
#print(faker.company())
#print(faker.job())

#print(faker.date_between(start_date=date(2025, 1, 1), end_date=date(2026, 12, 31)))
#print(faker.profile())

# Create a list of 50 employees
#employees =[]

#for _ in range(50):
#    employees.append({"name": faker.name(), "email": faker.email(), "job_title": faker.job(), "salary": faker.random_number(digits=5), "start_date": faker.date_this_decade()})

#print(len(employees))

# Write faker data into a csv file

def generate_employee():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "job_title": faker.job(), 
        "salary": faker.random_int(min=24000, max=99000), #this still writes a string into csv file - everything is a string in csv
        "start_date": faker.date_this_decade()
    }


# Write to csv file
with open("data/employees.csv", "w", newline="") as csv_file: 
    field_names=["name", "email", "job_title", "salary", "start_date"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for i in range(100):
        writer.writerow(generate_employee())