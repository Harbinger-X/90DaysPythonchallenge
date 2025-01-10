num = int(input("Input a non-negative number you want to find its factorial: "))

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of", num, "is", factorial(num) if num >= 0 else "not defined for negative numbers.")

#Note if a user inputs a float or a double, the program will throw an error.