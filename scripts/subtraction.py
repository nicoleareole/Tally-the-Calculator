# Tally the Calculator - Subtraction Module
def subtraction_operation():
    # Introduction and explanation of subtraction
    print("SUBTRACTION")
    print("Subtraction is the process of taking one number away from another.")
    print("For example, if you have 5 apples and you give away 2 apples, you would have 3 apples left.")
    print("In mathematical terms, this is written as 5 - 2 = 3.")
    print("Let's practice some subtraction problems together!")
    print("You can enter two numbers, and I will subtract the second number from the first for you.")

    # User input for subtraction
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number - second_number
        print(f"The result of {first_number} - {second_number} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

    # Explanation of subtraction terms
    print("Each of the numbers in a subtraction problem has a name:")
    print("1. The first number is called the 'minuend'.")
    print("2. The second number is called the 'subtrahend'.")
    print("3. The result is called the 'difference'.")
    print("Let's try another example!")
    first_number = input("Enter the minuend: ")
    second_number = input("Enter the subtrahend: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number - second_number
        print(f"The result of the minuend, {first_number}, subtracted by (-) the subtrahend, {second_number}, results in the difference {result}.")
    except ValueError:
        print("Please enter valid numbers.")
        
    # Explanation of why the order of numbers matters in subtraction
    print("Unlike addition, the order of numbers in subtraction matters. This means that changing the order of the minuend and subtrahend will change the result.")
    print("For example, 5 - 2 is not the same as 2 - 5. The first equals 3, while the second equals -3.")
    print("Let's try this out with some numbers!")
    first_number = input("Enter the minuend: ")
    second_number = input("Enter the subtrahend: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result1 = first_number - second_number
        result2 = second_number - first_number
        print(f"The result of {first_number} - {second_number} is {result1}.")
        print(f"The result of {second_number} - {first_number} is {result2}.")
        if result1 != result2:
            print("See? The difference changes when you switch the minuend and subtrahend!")
        else:
            print("Hmm, something went wrong. Let's check the numbers again.")
    except ValueError:
        print("Please enter valid numbers.")

    # Conclusion and encouragement
    print("Great job learning about subtraction! You can now practice subtracting numbers from each other.")
    print("Remember, subtraction is all about taking one number away from another to find the difference.")
    print("Keep practicing, and you'll become a subtraction expert in no time!")
    print("Thank you for using Tally the Calculator for your subtraction practice!")

    ## End of subtraction module