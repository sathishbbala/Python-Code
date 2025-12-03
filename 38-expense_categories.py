import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/expense_transactions.csv")

category_totals = (df.groupby("expense_category")["expense_amount"].sum())/100000
categories = category_totals.index.tolist() # creates a list of categories
totals = category_totals.values.tolist()    # creates a list of values 

fig, ax = plt.subplots(1, 1, figsize=(15,7))
bars = ax.bar(category_totals.index, category_totals.values)
ax.bar_label(bars, fmt='%.2f', rotation = 90, fontweight='bold', padding=3, label_type='center')
ax.set_xlabel("Category")
ax.set_ylabel("Total Expenses")
ax.set_title("Expense by Category")

plt.show()