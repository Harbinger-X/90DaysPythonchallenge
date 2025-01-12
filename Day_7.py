#This is a project about dictionaries  which is one of the four basic collection types for beginners in python
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#This project is about creating a dictionary that stores user information and allows the user to retrieve their information by entering their name.

User_info = {  } #Creating an empty dictionary to store user information
def add_user(): #Function to add a user to the dictionary
    name = input("Enter your name: ") #Asking the user for their name
    age = input("Enter your age: ") #Asking the user for their age
    email = input("Enter your email: ") #Asking the user for their email
    User_info[name] = [age,email] #Adding the user information to the dictionary
    print("User added successfully!") #Printing a message to confirm that the user has been added

def get_user(): #Function to get a user from the dictionary
    name = input("Enter your name: ") #Asking the user for their name
    if name in User_info: #Checking if the user exists in the dictionary
        print("Name: ", name)
        print("Age: ", User_info[name][0]) #Printing the user's age
        print("Email: ", User_info[name][1])
    else:
        print("User not found!")
        
def main(): #Main function to run the program
    while True: #Creating an infinite loop
        print("1. Add User") #Printing the menu
        print("2. Get User")
        print("3. Exit")
        choice = input("Enter your choice: ") #Asking the user for their choice
        if choice == "1": #Checking if the user chose to add a user
            add_user() #Calling the add_user function
        elif choice == "2": #Checking if the user chose to get a user
            get_user() #Calling the get_user function
        elif choice == "3": #Checking if the user chose to exit
            break #Exiting the loop
        else:
            print("Invalid choice!") #Printing a message if the user entered an invalid choice
            
if __name__ == "__main__": #Checking if the script is being run directly
    main() #Calling the main function