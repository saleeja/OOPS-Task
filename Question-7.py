"""7) Extend the above solution again and add another instance method called 'as_dict'. 
The method should return a dictionary with the data of the student. 
It should contain 'name', 'score', 'grade', keys and their respective values."""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade, self.congrats_message = self.calculate_grade()  # Calculate grade and get congrats message

    def calculate_grade(self):
        if not self.score.isdigit():   # Check if the entered score is a valid integer
            print("Invalid input for score. Please enter a valid integer.")
            return "INVALID", ""

        score_value = int(self.score)
         # Check if the score is greater than 100
        if score_value > 100:
            print("Invalid score.")
            return "INVALID", ""

        if score_value >= 90:
            return "A+", "Congratulations! You've achieved an excellent grade."
        elif score_value >= 80:
            return "A", "Great job! You've earned a very good grade."
        elif score_value >= 70:
            return "B+", "Well done! You've earned a good grade."
        elif score_value >= 60:
            return "B", "Good work! You've achieved a satisfactory grade."
        elif score_value >= 50:
            return "C+", "Keep it up! You've passed with a fair grade."
        elif score_value >= 40:
            return "C", "You've passed. Work on improvement for a better grade next time."
        else:
            return "FAILED", "Sorry, you've failed. Better luck next time."
 # Method to display student details
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Score: {self.score}")
        print(f"Student Grade: {self.grade}")
        print(f"\n{self.congrats_message}")

    def as_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.grade
        }

# Get user input for creating a Student instance
name = input("Enter the student's name: ")
score = input("Enter the student's score: ")

# Create a Student instance with user input
student = Student(name=name, score=score)

if student.grade != "INVALID":
    print("\nStudent Details:")
    student.display()

    # Display the student's data as a dictionary
    student_dict = student.as_dict()
    print("\nStudent Data as Dictionary:")
    print(student_dict)
