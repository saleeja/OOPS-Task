"""5) Create a class named Student with name, score as instance attributes. 
Assign values to both of these attributes using a constructor.
Create 2 Student objects. 
And also define a method called 'display' in the Student class - which, when called should print the name and score of the student.
"""


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        # Method to display the name and score of the student
        print(f"Student Name: {self.name}")
        print(f"Student Score: {self.score}")

# Creating two instances of the Student class
student1 = Student(name="sali", score=85)
student2 = Student(name="saleeja", score=92)

# Displaying details of the first and second student 
print("Details of Student 1:")
student1.display()

print("\nDetails of Student 2:")
student2.display()
