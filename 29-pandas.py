from datetime import datetime, timedelta
import pandas as pd

# Load into pandas 
df = pd.read_csv("data/expense_transactions.csv")
print(df.head())
print(df.loc[df["expense_amount"].idxmax()]) # Gets the highest expense amount 

# use this to learn pandas 
df["expense_date"] = pd.to_datetime(df["expense_date"]) # converts to date time data type 
df["year_month"] = df["expense_date"].dt.to_period("M")
monthly_summary = df.groupby("year_month")["expense_amount"].sum() 
print(monthly_summary)

summary_by_employee = df.groupby("emp_name")["expense_amount"].sum()
print(summary_by_employee)