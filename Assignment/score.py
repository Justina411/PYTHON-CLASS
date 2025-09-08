def grade_checker():
    while True:
        try:
            score = int(input("Enter your score (0-100): "))

            if score < 0 or score > 100:
                print("Invalid score! Please enter a number between 0 and 100.\n")
                continue  # ask again

            # Assign grades
            if score >= 90:
                grade = "A"
                message = "Excellent work! Keep it up!"
            elif score >= 80:
                grade = "B"
                message = "Great job! You're doing really well."
            elif score >= 70:
                grade = "C"
                message = "Good effort! You can aim even higher."
            elif score >= 60:
                grade = "D"
                message = "You passed, but there’s room for improvement."
            else:
                grade = "F"
                message = "Don’t give up! Keep practicing and you’ll get better."

            print(f"\nYour grade is {grade}. {message}")
            break  

        except ValueError:
            print("Invalid input! Please enter a number (0-100).\n")

grade_checker()
