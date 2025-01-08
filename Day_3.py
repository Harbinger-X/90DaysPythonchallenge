#This is a simple age checker program that checks the age of the user and determines if the user is eligible to buy a car or not.
name = str(input("Please enter your name: "))
print(f"Welcome {name} to Daps Automobile company")
age=int(input("please enter your age "))
if  age < 0:
    print("please enter a valid age")
elif age < 15:
    print("You are under 15. Access Restricted .")
elif age >= 15 and age < 18:
    print(f"Hello {name} are 15 or older but under 18. You can buy a car with parental consent.")
else:
    print(f"{name} are 18 or older. Hello  choose a car of choice ")
    
#NOTE TO THE END USER this program will crash when user enters anything other than a number as exception handling has not been implemented