#tThis project is to help me learn more about lists and tuples in python
#tI will be creating a program that will take a list of numbers and return the sum and average of the numbers in the list
numbers  = list (range(1,10))
total_Sum = sum(numbers )# This is to get the sum using sum() function

# This is to get the average
count = len(numbers) #The len() function calculates the number of elements in the list.
average = total_Sum / count
print(f"Sum: {total_Sum}")
print(f"Average: {average}") 

#But if we are to accept a users input to calculate the sum and average of the numbers in the list, we can use the code below


user_input = input("Enter your numbers separated by spaces: ").split()  # Take user input for numbers separated by spaces

numbers = [int(x) for x in user_input]   # Convert each item in the list to an integer

print(f"The numbers you typed were: {numbers}") # Print the numbers entered by the user

total_Sum = sum(numbers) # Calculate the sum of the numbers
average = total_Sum/len(numbers) # Calculate the average of the numbers
print(f"Sum: {total_Sum}")
print(f"Average: {average}")