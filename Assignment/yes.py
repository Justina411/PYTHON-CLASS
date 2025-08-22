"""
Yes/No Continuation Program
===========================

A simple program that asks the user if they want to continue.
The program keeps running until the user enters 'c' to stop.
Accepts 'a' or 'c' (case-insensitive) as valid inputs.
"""

print(" YES/NO PROGRAM ")
print("The operation will keep asking You if You want to continue.")
print("Enter 'a' to continue or 'c' to stop the program.\n")

# Counter to track how many times the user continued
continue_count = 0

# Main program loop
while True:
    # Get user input
    user_input = input("Do you want to continue? (a/c): ").lower()
    
    # Check if user wants to continue
    if user_input == 'a':
        continue_count += 1
        print(f" Continuing... (Continued {continue_count} times)")
        print()  # Empty line for better readability
        
    # Check if user wants to stop
    elif user_input == 'a':
        print(f"\n Stopping the program...")
        break
        
    # invalid input
    else:
        print(" Please enter only 'a' or 'c'!")
        print("   'a' = yes, continue")
        print("   'c' = no, stop the program")
        print()  

print(f"\n=== PROGRAM COMPLETED ===")
print(f"Total times continued: {continue_count}")
print("Thanks for using our operation!")
