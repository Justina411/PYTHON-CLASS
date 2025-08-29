print("What is your first number?")
num1 = int(input("Number 1: "))

print("What is your second number?")
num2 = int(input("Number 2: "))

print("What operation do you want to perform on the numbers?")
operation = input("Operation: ").lower()

def addition():
    sum = num1 + num2
    print

def diff():
    difference = num1 + num2
    print(difference)

def divide():
    quotient = num1 + num2
    print(quotient)

def multiply():
    multiply = num1 + num2
    print(multiply)


if operation == "sum":
    sum = num1 + num2 
    print(f"This is the sum of the two numbers; {sum}") #addition
  

elif operation == "difference":
    difference = num1 - num2
    print(f"This is the difference of the two numbers; {difference}") #subtraction 

elif operation == "product":
    product = num1 * num2
    print(f"This is the product of the two numbers; {product}") #multiplication 

elif operation == "quotient":
    if num2 == 0:
        print("Division by zero(0) is not possible.")
    
    else:
        quotient = num1 / num2
        print(f"This is the quotient of the two numbers; {quotient}") #division

else:
    print("Operation unavailable. Input operation again.")
    operation = input("Operation: ").lower()