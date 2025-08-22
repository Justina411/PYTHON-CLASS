"""
Positive Numbers operation
""

An easy operation that collects integer inputs from the user
and only stops operating when the user enters a negative number.
"""

print(" POSITIVE NUMBERS ")
print("Enter positive numbers (or zero) to continue.")
print("Enter a negative number to stop the operation.\n")

# Keeping track of the how many numbers inputed
number_count = 0

# loop
while True:
    try:
        # User input
        user_input = input("Enter number: ")
        
        # integer(number)
        number = int(user_input)
        
        # negative checker
        if number < 0:
            print(f"\nNegative number ({number}) seen!")
            print("Program ending...")
            break
        
        # If number is positive or zero, continue
        number_count += 1
        print(f" Number {number} ackowledged! (Total numbers: {number_count})")
        
    except ValueError:
        print(" Please enter a valid number!")

print(f"\n Operation Finished ")
print(f"Total positive numbers/zero entered: {number_count}")
print("Thanks for using our operation")
