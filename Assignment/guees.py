"""
Guess the Number Game
""


Guess game continues until the user guesses correctly.
"""

print(" GUESS THE NUMBER GAME ")
print("Try to guess the secret number between 1 and 10!\n")

# Secret number
secret_number = 7

# guess counter
attempts = 0

# Game
while True:
    try:
       # User guess
        guess = int(input("Enter your guess (1-10): "))
        attempts += 1
        
        # Guess number correct or wrong
        if guess == secret_number:
            print(f" Correct! You win!")
            print(f"It took you {attempts} attempt(s) to guess the number.")
            break
        else:
            print(" Wrong guess! Try again.\n")
            
    except ValueError:
        print("  Please enter a valid number!\n")

print("\n FINISHED ")
