from datetime import date
from write_data import WriteData
from generate_csv import DataGenerator
from setup_tables import CreateSQLTables
from crud import ExpenseTransactions

generate_data = input("Do you want new data to be generated again? (Y/N):")
if generate_data == "Y":
    while True:
        try:
            num_employees = int(input("How many employee records do you need?"))
            break
        except ValueError:
            print("Please Enter a valid integer")
    print("Data Generation in progress")
    dg = DataGenerator()
    dg.GenerateEmployee(num_employees)
    dg.GenerateCategories()
    print("Creating SQL Tables if the tables do not exist")
    ct = CreateSQLTables()
    ct.CreateTables()
    print("Writing Data from excel file into Tables")
    wd = WriteData()
    wd.WriteEmpData()
    wd.WriteCategoryData()
elif generate_data == "N":
    print("Skipping data generation step")
    data_operation = input("Do you want to Add or Modify or Delete an expense? (A/M/D):")
    if data_operation == "A": 
        et = ExpenseTransactions()
        et.AddExpense
    elif data_operation == "M":
        et = ExpenseTransactions()
        et.ModifyExpense
    elif data_operation == "D":
        et = ExpenseTransactions()
        et.DeleteExpense
else:
    print("Unknown Input, Skipping data generation step")




