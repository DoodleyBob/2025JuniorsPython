def check_even_odd(x2):

    # Use if/else to check if the number is even or odd
    if num % 2 == 0:
        print("The number is an even number!")
    else: 
        print("The number is an odd number!")

# Get user input
num = int(input("Enter a whole number: "))

# Call the function to run the program
check_even_odd(num)