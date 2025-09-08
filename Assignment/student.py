"""

A Very Simple Student Grade Tracker

Create a dictionary where keys are student names and values are lists of their test scores
Add functions to:

Add a new student
Add a grade for existing student
Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table
"""

# Student Grade Tracker

# Dictionary to store student names as keys and their grades as values (list of numbers)
students = {}

# Function to add a new student
def add_student(name):
    if name in students:
        print(f"{name} already exists.")
    else:
        students[name] = []
        print(f"Student {name} added.")

# Function to add a grade to a student
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")
    else:
        print(f"Student {name} not found. Please add them first.")

# Function to calculate average grade for a student
def average_grade(name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return None  # No grades available

# Function to display all students and their grades in a table
def display_all():
    if not students:
        print("No students available.")
        return
    print("\n===== Student Grades =====")
    print(f"{'Name':<15}{'Grades':<25}{'Average':<10}")
    for name, grades in students.items():
        avg = average_grade(name)
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"{name:<15}{str(grades):<25}{avg_display:<10}")

# ------------------------------
# Example usage

add_student("Alice")
add_student("Bob")

add_grade("Alice", 90)
add_grade("Alice", 80)
add_grade("Bob", 75)
add_grade("Bob", 85)

display_all()
