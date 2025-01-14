# Write a Python program to get a number from the user and print it. If the user enters an invalid input, catch the exception and print an error message.


try:
    num = int(input("Enter a number: "))  # Get user input
    print(f"You entered: {num}")# Print the number
except ValueError: # This block will run if a ValueError is raised
    print("Invalid input! Please enter a valid number.")#