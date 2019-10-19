#Start of a program
#Math Program

def add(num1, num2):
    sum = num1 + num2
    print("Your numbers", str(num1), "+", str(num2), "=", sum)

def sub(num1, num2):
    sum = num1 - num2
    print("Your numbers", str(num1), "-", str(num2), "=", sum)

def mult(num1, num2):
    sum = num1*num2
    print("Your numbers", str(num1), "x", str(num2), "=", sum)

def div(num1, num2):
    sum = num1/num2
    print("Your numbers", str(num1), "/", str(num2), "=", sum)

def sel_after_math():
    choice = input("Do you want to do this again? (y/n)")
    choice = choice.lower()
    while choice != "n":
        if choice == "y" or choice == "Y":
            menu()
        else:
            print("You entered invalid choice")
            sel_after_math()
    print("Goodbye!")
    exit()

def menu():
    print("Menu: \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n x - Exit")
    selection = input("Selection: ")
    selection = selection.lower()

    while selection != "x":
        if selection == "1":
            num1 = input("Enter first number: ")
            num1 = int(num1)
            num2 = input("Enter second number: ")
            num2 = int(num2)
            add(num1, num2)
            sel_after_math()

        elif selection == "2":
            num1 = input("Enter first number: ")
            num1 = int(num1)
            num2 = input("Enter second number: ")
            num2 = int(num2)
            sub(num1, num2)
            sel_after_math()

        elif selection == "3":
            num1 = input("Enter first number: ")
            num1 = int(num1)
            num2 = input("Enter second number: ")
            num2 = int(num2)
            mult(num1, num2)
            sel_after_math()

        elif selection == "4":
            num1 = input("Enter first number: ")
            num1 = int(num1)
            num2 = input("Enter second number: ")
            num2 = int(num2)
            div(num1, num2)
            sel_after_math()

        else:
            print("Enter your selection again!")
            menu()

    print("Goodbye!")
    exit()

print("Welcome to the simple calculator")
menu()
