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
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def print_details(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)  # Inherit from Staff
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        super().print_details()


teachers_list = [
    Teacher(name="saleeja", age=28, role="Teacher", department="Science", salary=50000),
    Teacher(name="Sara", age=35, role="Teacher", department="Math", salary=55000),
    # Add more teachers as needed
]

  # Function to find a teacher by name in the teachers_list
def find_teacher_by_name(name):
    for teacher in teachers_list:
        if teacher.name.lower() == name.lower():
            return teacher
    return None

def add_teacher():
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    role = input("Enter the role: ")
    department = input("Enter the department: ")
    salary = float(input("Enter the salary: "))

    new_teacher = Teacher(name=name, age=age, role=role, department=department, salary=salary)
    teachers_list.append(new_teacher)
    print(f"Teacher {name} added successfully!")

# Get user input for searching a teacher
search_name = input("Enter the teacher's name to search: ")
found_teacher = find_teacher_by_name(search_name)

if found_teacher:
    found_teacher.print_details()
else:
    print(f"Teacher with name {search_name} not found.")
    add_option = input("Do you want to add a new teacher? (yes/no): ").lower()
    if add_option == "yes":
        add_teacher()


# output
        
# if found
"""        
Enter the teacher's name to search: saleeja
Name: saleeja      
Age: 28
Role: Teacher      
Department: Science
Salary: 50000 """

# if not found

"""
Enter the teacher's name to search: sal
Teacher with name sal not found.
Do you want to add a new teacher? (yes/no): yes
Enter the name: joe
Enter the age: 23
Enter the role: teacher
Enter the department: ece 
Enter the salary: 50000
Teacher joe added successfully!"""