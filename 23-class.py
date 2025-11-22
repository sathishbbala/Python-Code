import random

class Student:
    def __init__(self, name, gender, program):
        self.name = name
        self.gender = gender
        self.program = program
    
    def change_program(self, new_program):
        self.program = new_program


S1 = Student("Alice", "Female", "MBA")
S1.change_program("Msc")

print(f"Student Name: {S1.name} doing {S1.program}")
