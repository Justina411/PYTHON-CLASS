# num1 = int("Enter first number: ")
# num2 = int("Enter the second number: ")

# def greet(name):
#     print(f"Hello User {name}")
# greet(myName)

# def add(a, b):
#     print(a + b)

# add(num1, num2)

# def add2(num1,num2):
#     sum = num1 + num2
#     print(f"this is the sum: {sum}")

# add2(10 , 5)


# bakeryList = ["bread", "Cake", "Donuts", "Cookies", "muffins", "Strawberry cake"]

# def CheckStock(pastry):
#            counter = 0
#            for item  in pastry:
#                 if item != "Strawberry cake":
#                     counter +=1
#                     print(counter, "loop")
#                     print("Yess we have it in stock")
#                     continue
#                 else:
#                    print("we out of stock")
# CheckStock(bakeryList)

classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi" ]

def clas(name):
    for namer in name:
        if namer != "actress":
            print("loop")
            print("Yess am here")
            continue
    else:
        print("Am not an actress")
clas(classList)