# Tally the Calculator - Division Module
def division_operation():
    # Introduction and explanation of multiplication
    print ("DIVISION")
    print("Division is the process of splitting a number into equal parts or groups.")
    print("For example, if you have 12 apples and you want to divide them into 4 equal groups, you would have 3 apples in each group.")
    print("In mathematical terms, this is written as 12 / 4 = 3.")
    print("Let's practice some division problems together!")
    print("You can enter two numbers, and I will divide the first number by the second for you.")

    # User input for division
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        if second_number == 0:
            print("Division by zero is not allowed. Please enter a non-zero second number.")
        else:
            result = first_number / second_number
            print(f"The result of {first_number} / {second_number} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

    # Explanation of division terms
    print("Each of the numbers in a division problem has a name:")
    print("1. The first number is called the 'dividend'.")
    print("2. The second number is called the 'divisor'.")
    print("3. The result is called the 'quotient'.")
    print("Let's try another example!")
    first_number = input("Enter the dividend: ")
    second_number = input("Enter the divisor: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        if second_number == 0:
            print("Division by zero is not allowed. Please enter a non-zero divisor.")
        else:
            result = first_number / second_number
            print(f"The result of the dividend, {first_number}, divided by (/) the divisor, {second_number}, results in the quotient {result}.")
    except ValueError:
        print("Please enter valid numbers.")
        
    # Explanation for why dividing by zero is not allowed
    print("It's important to note that division by zero is not allowed in mathematics. This is because dividing by zero does not yield a meaningful result. For example, if you try to divide 5 by 0, you are essentially asking how many times 0 can fit into 5, which is not possible. Therefore, always ensure that the divisor is a non-zero number.")

    # Explanation of why the order of numbers matters in division
    print("Unlike addition and multiplication, the order of numbers in division matters. This means that changing the order of the dividend and divisor will change the result.")
    print("For example, 12 / 4 is not the same as 4 / 12. The first equals 3, while the second equals 0.3333.")
    print("Let's try this out with some numbers!")
    first_number = input("Enter the dividend: ")
    second_number = input("Enter the divisor: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        if second_number == 0:
            print("Division by zero is not allowed. Please enter a non-zero divisor.")
        else:
            result1 = first_number / second_number
            result2 = second_number / first_number
            print(f"The result of {first_number} / {second_number} is {result1}.")
            print(f"The result of {second_number} / {first_number} is {result2}.")
            if result1 != result2:
                print("See? The quotient changes when you switch the dividend and divisor!")
            else:
                print("Hmm, something went wrong. Let's check the numbers again.")
    except ValueError:
        print("Please enter valid numbers.")

    # Conclusion and encouragement
    print("Great job learning about division! You can now practice dividing numbers.")
    print("Remember, division is all about splitting a number into equal parts or groups.")
    print("Keep practicing, and you'll become a division expert in no time!")
    print("Thank you for using Tally the Calculator for your division practice!")

    ## End of division module