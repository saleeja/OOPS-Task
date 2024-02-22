"""6) Extend the above solution and add another instance attribute called grade (should be string). 
Assign value to grade from within the constructor.
The value should not be taken from user input.
Instead use the following conditions and assign values to grade by using the value of score.
grade = A+ if score >=90
grade = A if score >=80 and <90
grade = B+ if score >=70 and <80
and so on.
if score is below 40 then grade should be "FAILED"
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade,self.congrats_message = self.calculate_grade()

    def calculate_grade(self):
        while True:
            if not self.score.isdigit(): # Check if the entered score is a valid integer
                print("Invalid input for score. Please enter a valid integer.")
                return "INVALID"
                break
        
            else:
                score_value = int(self.score)
                 # Check if the score is greater than 100
                if score_value > 100:
                    print("Invalid score.")
                    return "INVALID" ,""
                
                elif score_value >= 90:
                    return "A+", "Congratulations! You've achieved an excellent grade."
                elif score_value >= 80:
                    return "A" ,"Great job! You've earned a very good grade."
                elif score_value >= 70:
                    return "B+" ,"Well done! You've earned a good grade."
                elif score_value >= 60:
                    return "B" ,"Good work! You've achieved a satisfactory grade."
                elif score_value >= 50:
                    return "C+","Keep it up! You've passed with a fair grade."
                elif score_value >= 40:
                    return "C" ,"You've passed. Work on improvement for a better grade next time."
                else:
                    return "FAILED" , "Sorry, you've failed. Better luck next time."
 # Method to display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.grade}")
        print(f"\n{self.congrats_message}")


# Get user input for creating a Student instance
name = input("Enter the student's name: ")
score = (input("Enter the student's score: "))

# Create a Student instance with user input
student = Student(name=name, score=score)

if student.grade != "INVALID":
    print("\nStudent Details:")
    
    student.display()

# output
"""
Student Details:
Name: saleeja
Score: 100
Grade: A+

Congratulations! You've achieved an excellent grade."""