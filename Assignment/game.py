# This is a code to give even numbers and odd numbers 
def numbers():
    try:
        num = int(input("Enter a number "))
        if num % 2 == 0 :
            print( f"{num} is an even number ")
        elif num % 2 == 1 :
            print(f"{num} is an odd number")
    except ValueError:
        print("invalid input")

numbers()


