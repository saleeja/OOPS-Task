"""8) show class method, static method and instance method with simple example."""

class ExampleClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Instance Method
    def instance_method(self):
        print(f"Instance Method: Accessing instance variable - {self.instance_variable}")

    @classmethod
    # Class Method
    def class_method(cls):
        print(f"Class Method: Accessing class variable - {cls.class_variable}")

    @staticmethod
    # Static Method
    def static_method():
        print("Static Method: No access to instance or class variables")


# Creating an instance of the class
example_instance = ExampleClass(instance_variable="I am an instance variable")

# Calling instance method
example_instance.instance_method()

# Calling class method
ExampleClass.class_method()

# Calling static method
ExampleClass.static_method()
