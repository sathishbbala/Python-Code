import json

#TODO #1: Load data.json into a dictionary and print it
with open('employees.json', 'r') as file:
    data = json.load(file)
    print(data) 

#TODO #2: Print all the employees in the Engineering department
for employee in data["employees"]:
    if employee["department"] == "Engineering":
        print(employee)


#TODO #3: Print a list of unique skills possessed by employees
unique_skills = set()
for employee in data["employees"]:
    for skill in employee["skills"]:
        unique_skills.add(skill)
print(list(unique_skills))

#TODO #4: Find the average salary of Engineering employees
total_salary = 0
count = 0
for employee in data["employees"]:
    if employee["department"] == "Engineering":
        total_salary += employee["salary"]
        count += 1 
average_salary = total_salary / count if count > 0 else 0   
print(f"Average salary of Engineering employees: {average_salary}")

#TODO #5: List all employees who has worked on Project Atlas 
# data["employees"] is a list of employee dictionaries
# Each element inside the list is a dictionary representing an employee
# Projet is a list inside the dictionary with name  and status as elements
for employee in data["employees"]:
    for project in employee["projects"]:
        if project["name"] == "Project Atlas":
            print(employee["name"])
        
#TODO #6: Add a new employee
new_employee = {
    "id": 104,
    "name": "David Park",
    "department": "Engineering",
    "skills": ["Go", "Kubernetes"],
    "salary": 99000,
    "projects": []
}
data["employees"].append(new_employee)
print(data["employees"])

#TODO #7: Add a new skill CI/CD to all employees in the Engineering department
for employee in data["employees"]:
    if employee["department"] == "Engineering":
        if "CI/CD" not in employee["skills"]:
            employee["skills"].append("CI/CD")
print(data["employees"])

#TODO #8: Save the updated json into a new file updated_employees.json 
with open("updated_employees.json", "w") as f:
    json.dump(data, f, indent=4)