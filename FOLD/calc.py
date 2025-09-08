"""
This is a code to print out the;
Sum of two numbers
Difference of two numbers
Product of two numbers
Quotient of two numbers
"""

while True:

    print("What is your first number?")
    num1 = int(input("Number 1: "))

    print("What is your second number?")
    num2 = int(input("Number 2: "))

    print("What operation do you want to perform on the numbers?")
    operation = input("Operation: ").lower()

    def sum():
        sum = num1 + num2 
        print(f"This is the sum of the two numbers; {sum}") #addition

    def difference():
        difference = num1 - num2
        print(f"This is the difference of the two numbers; {difference}") #subtraction

    def product():
        product = num1 * num2
        print(f"This is the product of the two numbers; {product}") #multiplication 

    def quotient():
        if num2 == 0:
            print("Division by zero(0) is not possible.")
        
        else:
            quotient = num1 / num2
            print(f"This is the quotient of the two numbers; {quotient}") #division


    if (operation == "sum"):
        sum()

    elif (operation == "difference"):
        difference()

    elif (operation == "product"):
        product()

    elif (operation == "quotient"):
        quotient()
        
    else:
        print("Operation unavailable. Input operation again.")
        continue

    print("Do you want to continue?")
    choice = input("Choice: ")
    if(choice == "y"):
        continue
    elif(choice == "n"):
        print("Program Terminated")
        break
    else:
        print("invalid input. Program Terminated.")




# sum = num1 + num2 
# print(f"This is the sum of the two numbers; {sum}") #addition

# difference = num1 - num2
# print(f"This is the difference of the two numbers; {difference}") #subtraction

# product = num1 * num2
# print(f"This is the product of the two numbers; {product}") #multiplication

# quotient = num1 / num2
# print(f"This is the quotient of the two numbers; {quotient}") #division