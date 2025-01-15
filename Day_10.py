import math

while True:
    # Get user input
    user_input = input("Enter a number to calculate its square root: ")
    
    try:
        # Check if input contains any letters
        if any(char.isalpha() for char in user_input):
            print("Error: Letters are not allowed! Please enter a number only.")
            continue
            
        # Convert to float and check if it's a valid number
        number = float(user_input)
        
        # Check if number is non-negative
        if number >= 0:
            square_root = math.sqrt(number)
            print(f"The square root of {number} is: {square_root}")
            break
        else:
            print("Error: Cannot calculate square root of a negative number!")
            
    except ValueError:
        print("Error: Invalid input! Please enter a valid number.")
        print("Examples of valid input: 16, 25.5, 4")