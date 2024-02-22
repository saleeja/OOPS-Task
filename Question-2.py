"""2)Write a program that prints the class name using its object."""

class ClassName:
    def __init__(self, name):
         # Constructor method (__init__) initializes the object's attributes
        self.name = name

    def print_class_name(self):
        # Method to print the class name using __class__.__name__
        print(f"Class name using __class__: {self.__class__.__name__}") #self.__class__ refers to the class of the current instance. 
        #__name__ retrieves the name of that class.
obj = ClassName("My Object")
obj.print_class_name()



# using type() method
# built-in type() function, which takes an object as input and returns the class it belongs to
# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def print_class_name(self):
#         print(f"Class name using type(): {type(self).__name__}")

# obj = MyClass("My Object")
# obj.print_class_name()
