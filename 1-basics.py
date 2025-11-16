# Basic Python Program 
# mydict is a list and each element is a dict 
# Skills is a list within the dictionary

mydict = [
{"Name": "Alice", "Age": 33, "Role": "Principal Architect", "City": "Chennai", "Skills": ["Python", "AWS", "Java"] },
{"Name": "Allan", "Age": 31, "Role": "Senior Architect", "City": "Chennai", "Skills": ["Python", "AWS", "Java"] },
{"Name": "Bob", "Age": 28, "Role": "Senior Developer", "City": "Chennai", "Skills": ["Python", "AWS", "Java"] },
{"Name": "David", "Age": 25, "Role": "Junior Developer", "City": "Chennai", "Skills": ["Python", "AWS", "Java"] }
]

print(type(mydict[0])) # output will be dict
print(mydict[0]['Name']) # output will be Alice

for employee_details in mydict:
    if employee_details['Name'] == "Alice":
        employee_details['Skills'].append("Ci/CD")
        print(employee_details['Skills'])

print(mydict)








