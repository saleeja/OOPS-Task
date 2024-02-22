"""8) show class method, static method and instance method with simple example."""

class Teacher:
    school_name = "ABC School"  # Class variable

    def __init__(self, name, subject):
        self.name = name  # Instance variable
        self.subject = subject  # Instance variable

    # Instance Method
    def display_teacher_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"School: {Teacher.school_name}")  # Accessing class variable

    @classmethod
    # Class Method
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to {cls.school_name}")

    @staticmethod
    # Static Method
    def welcome_message():
        print("Welcome to the teaching profession!")

# Creating an instance of the Teacher class
teacher1 = Teacher(name="Mr. joe", subject="Maths")

# Calling instance method
print("Instance Method:")
teacher1.display_teacher_info()

# Calling class method
print("\nClass Method:")
Teacher.change_school_name(new_name="XYZ School")
teacher1.display_teacher_info()  # The class variable is updated for all instances

# Calling static method
print("\nStatic Method:")
Teacher.welcome_message()

# output

# School: ABC School

"""Class Method:
School name changed to XYZ School
Teacher Name: Mr. joe
Subject: Maths
School: XYZ School

Static Method:
Welcome to the teaching profession!"""


