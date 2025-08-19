# This is a program that gives the greater as output
  
def number():
    try:
        num1 = int(input("Enter a number "))
        num2 = int(input("Enter a number "))
        if num1 > num2 :
            print(f"{num1} is greater ")
        else:
            print(num2)  
    except ValueError:
        ("invalid space ")

number()
