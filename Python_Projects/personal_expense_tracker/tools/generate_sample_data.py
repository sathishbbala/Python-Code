from faker import Faker
from datetime import date
from csv import writer, DictReader, DictWriter
import csv
faker = Faker("en_US") # setting US to get localized data

class DataGenerator:
    def generate_employees_csv(self, num_records):
        with open("database/seed_data/employees.csv", "w", newline="") as csv_file: 
            field_names=["name", "email", "job_title", "salary", "start_date"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for i in range(num_records):
                employee_record = {
                        "name": faker.name(),
                        "email": faker.email(),
                        "job_title": faker.job(), 
                        "salary": faker.random_int(min=24000, max=99000), #this still writes a string into csv file - everything is a string in csv
                        "start_date": faker.date_this_decade()
                 }
                writer.writerow(employee_record)

    def generate_categories_csv(self):
        categories = ["Travel","Meals","Accommodation","Software","Hardware","Training","Taxi","Internet","Office Supplies","Team Event"]
        with open("database/seed_data/categories.csv", "w", newline="") as csv_file: 
            writer = csv.writer(csv_file)
            writer.writerow(["category"])
            for category in categories: 
                writer.writerow([category])
