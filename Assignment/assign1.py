"""""
CONDITIONAL STATEMENT
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


operation = input("Choose operation (+, -, *, /): ")


if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Division by 0 is Null")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid input Please choose +, -, *, or /")



