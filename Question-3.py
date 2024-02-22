"""3)Write a Python class, Square, and define two methods that return the square area and perimeter."""

class Square:
    def __init__(self, length):
        # Constructor method initializes the side length of the square
        self.length = length

    def calculate_area(self):
        # Method to calculate the area of the square
        area = self.length ** 2
        return area

    def calculate_perimeter(self):
        # Method to calculate the perimeter of the square
        perimeter = 4 * self.length
        return perimeter

 # Getting user input 
user_input = (input("Enter the side length of the square: "))

if user_input.replace('.', '').isdigit():
    # Convert the input to a float if it is a valid number
    user_side_length = float(user_input)
   

    square_obj = Square(length=user_side_length)

    area_result = square_obj.calculate_area()
    print(f"Area of the square: {area_result}")

    perimeter_result = square_obj.calculate_perimeter()
    print(f"Perimeter of the square: {perimeter_result}")


else:
    print("Error: Invalid input. Please enter a valid number.")

# output
    
"""Enter the side length of the square: 2
Area of the square: 4.0
Perimeter of the square: 8.0"""


# if not entered number
"""Enter the side length of the square: s
Error: Invalid input. Please enter a valid number."""