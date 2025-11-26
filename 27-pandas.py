import pandas as pd
from datetime import date  

def calculate_tenure(date_of_hire):
    delta_in_days = date.today() - date_of_hire
    years = delta_in_days.days // 365
    months = (delta_in_days.days % 365) // 30
    return f"{years} years.{months} months"

def describe_employee(row):
    converted_to_date = pd.to_datetime(row.start_date).date()
    return f"{calculate_tenure(converted_to_date)}"

df = pd.read_csv("data/employees.csv")
df.to_csv("data/sample.csv", index=False)
df["tenure"] = df.apply(describe_employee, axis=1)
df.to_csv("data/sample.csv", index=False)