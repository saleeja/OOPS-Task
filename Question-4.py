"""4) Write a program to create a child class Teacher that will inherit the properties from the parent class Staff.
    attributes need for staff : role,department, salary
    attributes need for teacher: name,age
    method in  staff : def print_details()

    output expected -
        Name:  Raj
        Age:  28
        Role: Teacher
        Department: Science
"""


class Staff:

    def __init__(self,role,department,salary) -> None:
        self.role=role
        self.department=department
        self.salary=salary


    def print_details(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")



class Teacher(Staff):
    def __init__(self,name,age,role,department,salary) -> None:
        super().__init__(role, department, salary) # Inherit from Staff
        self.name=name
        self.age=age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        super().print_details()

obj=Teacher(name="Saleeja",age=24,role="Teacher",department="Science",salary=20000)
obj.print_details()