# Tally the Calculator - Addition Module
def addition_operation(): 
    # Introduction and explanation of addition
    print("ADDITION")
    print("Addition is the process of finding the total or sum by combining two or more numbers.")
    print("For example, if you have 2 apples and you get 3 more apples, you would have a total of 5 apples.")
    print("In mathematical terms, this is written as 2 + 3 = 5.")
    print("Let's practice some addition problems together!")
    print("You can enter two numbers, and I will add them for you.")

    # User input for addition
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number + second_number
        print(f"The result of {first_number} + {second_number} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")
        
    # Explanation of additon terms
    print("Each of the numbers in an addition problem has a name:")
    print("1. The first number is called the 'addend'.")
    print("2. The second number is also called an 'addend'.")
    print("3. The result is called the 'sum'.")
    print("Let's try another example!")
    first_number = input("Enter the first addend: ")
    second_number = input("Enter the second addend: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number + second_number
        print(f"The result of the first addend, {first_number}, added to (+) the sedond addend, {second_number}, results in the sum {result}.")
    except ValueError:
        print("Please enter valid numbers.")

    # Explanation of commutative property of addition
    print("When it comes to addition, it does not matter in which order you add the numbers. This is called the 'commutative property of addition'. You can switch the order of the addends, and the sum will still be the same.")
    print("For example, 2 + 3 is the same as 3 + 2, and both equal 5.")
    print("Let's try this out with some numbers!")
    first_number = input("Enter the first addend: ")
    second_number = input("Enter the second addend: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result1 = first_number + second_number
        result2 = second_number + first_number
        print(f"The result of {first_number} + {second_number} is {result1}.")
        print(f"The result of {second_number} + {first_number} is {result2}.")
        if result1 == result2:
            print("See? The sum is the same regardless of the order of the addends!")
        else:
            print("Hmm, something went wrong. Let's check the numbers again.")
    except ValueError:
        print("Please enter valid numbers.")
        
    # Conclusion and encouragement
    print("Great job learning about addition! You can now practice adding numbers together.")
    print("Remember, addition is all about combining numbers to find the total or sum.")
    print("Keep practicing, and you'll become an addition expert in no time!")
    print("Thank you for using Tally the Calculator for your addition practice!")

    ## End of addition module