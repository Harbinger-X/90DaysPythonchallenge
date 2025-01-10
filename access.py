# An access control system that greets users based on their role and grants access based on their role.

# Get the user's name
name = input("Please enter your name: ")
print(f"Welcome {name} to UMaT Portal!")

# Loop to ensure valid role input
while True:
    role = input("Please enter your role (admin/user/guest): ").lower()  # Convert to lowercase for case-insensitivity
    
    # Check if the input is a valid role
    if role in ["admin", "user", "guest"]:  # Check if the role is valid
        break  # Exit the loop if the input is valid
    else:
        print("Invalid role. Please enter 'admin', 'user', or 'guest'.")

# Granting  or denying  access based on role
if role == "admin":
    # Ask for admin password
    password = input("Enter admin password: ")
    if password == "admin123":  # PASSWORD: admin123
        print(f"Hello {name}, you have full access as an admin.")
    else:
        print("Incorrect password. Access denied.")
elif role == "user":
    print(f"Hello {name}, you have limited access as a user.")
else:
    print(f"Hello {name}, you have read-only access as a guest Welcome .")