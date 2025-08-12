# Tally the Calculator - Multiplication Module
def multiplication_operation():
    # Introduction and explanation of multiplication
    print("MULTIPLICATION")
    print("Multiplicatiion is the process of finding the total of one number added to itself a certain number of times.")
    print("For example, if you have 3 groups of 4 apples, you would have a total of 12 apples.")
    print("In mathematical terms, this is written as 3 * 4 = 12.")
    print("Let's practice some multiplication problems together!")
    print("You can enter two numbers and I will multiply them for you.")

    # User input for multiplication
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number * second_number
        print(f"The result of {first_number} * {second_number} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

    # Explanation of multiplication terms
    print("Each of the numbers in a multiplication problem has a name:")
    print("1. The first number is called the 'multiplicand'.")
    print("2. The second number is called the 'multiplier'.")
    print("3. The result is called the 'product'.")
    print("Let's try another example!")
    first_number = input("Enter the multiplicand: ")
    second_number = input("Enter the multiplier: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result = first_number * second_number
        print(f"The result of the multiplicand, {first_number}, multiplied by (*) the multiplier, {second_number}, results in the product {result}.")
    except ValueError:
        print("Please enter valid numbers.")

    # Explanation of commutative property of multiplication
    print("When it comes to multiplication, it does not matter in which order you multiply the numbers. This is called the 'commutative property of multiplication'. You can switch the order of the multiplicand and multiplier, and the product will still be the same.")
    print("For example, 3 * 4 is the same as 4 * 3, and both equal 12.")
    print("Let's try this out with some numbers!")
    first_number = input("Enter the multiplicand: ")
    second_number = input("Enter the multiplier: ")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
        result1 = first_number * second_number
        result2 = second_number * first_number
        print(f"The result of {first_number} * {second_number} is {result1}.")
        print(f"The result of {second_number} * {first_number} is {result2}.")
        if result1 == result2:
            print("See? The product is the same regardless of the order of the multiplicand and multiplier!")
        else:
            print("Hmm, something went wrong. Let's check the numbers again.")
    except ValueError:
        print("Please enter valid numbers.")

    # Conclusion and encouragement
    print("Great job learning about multiplication! You can now practice multiplying numbers together.")
    print("Remember, multiplication is all about finding the total of one number added to itself a certain number of times.")
    print("Keep practicing, and you'll become a multiplication expert in no time!")
    print("Thank you for using Tally the Calculator for your multiplication practice!")

    ## End of multiplication module