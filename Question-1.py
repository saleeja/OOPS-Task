"""1)Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object."""

class Student:
    def __init__(self, name,lastname, age, grade):
        self.name = name   #instance variable
        self.lastname=lastname
        self.age = age
        self.grade = grade
       

# prints a summary of the student's information
    def print_summary(self):
        print(f"Student Name: {self.name}{self.lastname}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        
        

# Creating an instance of the class
student1 = Student(name="Saleeja ",lastname="S",age=19, grade="A+")
student2 = Student(name="Ami ",lastname="A",age=18, grade="A+")

# Using the print_summary function
print("Roll number 1:")
student1.print_summary()
print()
print("Roll number 2:")
student2.print_summary()



# output
"""Roll number 1:
Student Name: Saleeja S
Age: 19
Grade: A+

Roll number 2:
Student Name: Ami A    
Age: 18
Grade: A+"""