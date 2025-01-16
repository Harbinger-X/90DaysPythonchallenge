import re

def validate_email(email):
    # Define the regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Main program
if __name__ == "__main__":
    # Ask the user for an email address
    user_email = input("Please enter an email address to validate: ")
    
    # Validate the email
    if validate_email(user_email):
        print(f"✅ The email '{user_email}' is valid.")
    else:
        print(f"❌ The email '{user_email}' is invalid.")