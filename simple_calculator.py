# Addition
def addition(num1,num2):
    return f"The addition of {num1} + {num2} = {addition(num1, num2)}"

#subtraction
def subtraction(num1,num2):
    return num1 - num2

# multiplication
def multiplication(num1,num2):
    return num1 * num2

# division
def division(num1,num2):
    return num1 / num2 if num2 else "Cannot divide by zero"

def menu():
    while True:
        print(""" Welcome to the Simple Calculator
        Select operation you want to perform:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit""")
        
        user_choice = input("Enter your choice (1-5): ")

        if user_choice == "5":
            print("You chose to exit!!!")
            print("Exiting the calculator. Goodbye!")
            break

        if user_choice == "1":
            print("You chose addition!!!")
            num1 = int(input("enter the value of the first number: "))
            num2 = int(input("enter the value of the second number: "))
            print(f"The addition of {num1} + {num2} = {addition(num1, num2)}")

        elif user_choice == "2":
            print("You chose subtraction!!!")
            num1 = int(input("enter the value of the first number: "))
            num2 = int(input("enter the value of the second number: "))
            print(f"The subtraction of {num1} - {num2} = {subtraction(num1, num2)}")

        elif user_choice == "3":
            print("You chose multiplication!!!")
            num1 = int(input("enter the value of the first number: "))
            num2 = int(input("enter the value of the second number: "))
            print(f"The multiplication of {num1} x {num2} = {multiplication(num1, num2)}") 

        elif user_choice == "4":
            print("You chose division!!!")
            num1 = float(input("enter the value of the first number: "))
            num2 = float(input("enter the value of the second number: "))
            print(f"The division of {num1} / {num2} = {division(num1, num2)}")

        else:
            print("Invalid choice. Please select a valid option from 1 - 5")
            continue

menu()