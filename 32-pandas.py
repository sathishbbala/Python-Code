import pandas as pd
from random import randint


student_list = ["Arjun", "Meera", "Rahul", "Ram", "Vidhya", "Samuel", "Raj", "Kumar", "Mani", "Mathura", "Venu", "Arya", "Arpit", "Arnav" ]
subject_list = ["English", "Maths", "Physics", "Chemistry", "Computer Science"]

students = {
    student: {
        subject: randint(60, 100)
        for subject in subject_list
    }
    for student in student_list
}

print(students)

# Load into data frame
df = pd.DataFrame.from_dict(students, orient="index") # Rows = Student Column = Marks
df.index.name = "Student"
# print(df)

# Find Total per student 
df["Student_Total"] = df.sum(axis=1) # adds a new column Average 
print(df)

# Add a new row which will have average marks per subject 
df.loc["Average_per_subject"] = df.mean().round(2)
print(df)

# Find the top scorer by subject 
highest_per_subject = df.max(axis=0)
print(highest_per_subject)

top_student_per_subject = df.idxmax()
print(top_student_per_subject)

summary = pd.DataFrame({
    "Highest_Mark": df.max(),
    "Topper": df.idxmax()
})
print(summary)
