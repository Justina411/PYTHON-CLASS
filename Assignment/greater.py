# This is a program that gives the greater as output
  
# def number():
#     try:
#         num1 = int(input("Enter a number "))
#         num2 = int(input("Enter a number "))
#         if num1 > num2 :
#             print(f"{num1} is greater ")
#         else:
#             print(num2)  
#     except ValueError:
#         ("invalid space ")

# number()



"""
get two int and return the greater
"""

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if (num1 == num2):
    print("The numbers are the same")
elif(num1 < num2):
    print(f"num2: {num2} is the greater number")
else:
    print(f"num1: {num2} is the greater")
