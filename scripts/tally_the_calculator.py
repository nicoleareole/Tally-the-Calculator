# Tally the Calculator script

# Import necessary modules
import addition
import subtraction
import multiplication
import division

# Define functions
def introduction_screen():
    print("WELCOME TO TALLY THE CALCULATOR")
    print("It's time to work on your math skills!")
    print("Please choose which operation you would like to learn about:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    operation_choice = input("Enter the number corresponding to your choice (1-5): ").strip()
    if operation_choice == '1':
        addition_operation()
    elif operation_choice == '2':
        subtraction_operation()
    elif operation_choice == '3':
        multiplication_operation()
    elif operation_choice == '4':
        division_operation()
    elif operation_choice == '5':
        print("Thank you for using Tally the Calculator! Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choose_operation()

def addition_operation():
    addition.addition_operation()
    next_operation()

def subtraction_operation():
    subtraction.subtraction_operation()
    next_operation()

def multiplication_operation():
    multiplication.multiplication_operation()
    next_operation()

def division_operation():
    division.division_operation()
    next_operation()

def choose_operation():
    print("Please choose which operation you would like to learn about:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    operation_choice = input("Enter the number corresponding to your choice (1-5): ").strip()
    if operation_choice == '1':
        addition_operation()
    elif operation_choice == '2':
        subtraction_operation()
    elif operation_choice == '3':
        multiplication_operation()
    elif operation_choice == '4':
        division_operation()
    elif operation_choice == '5':
        print("Thank you for using Tally the Calculator! Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choose_operation()

def next_operation():
    print("Would you like to try another operation? (yes/no)")
    user_response = input().strip().lower()
    if user_response == 'yes':
        choose_operation()
    else:
        print("Thank you for using Tally the Calculator! Goodbye!")

# Start the calculator
introduction_screen()
# This will display the introduction screen and allow the user to choose an operation.

# End of Tally the Calculator script