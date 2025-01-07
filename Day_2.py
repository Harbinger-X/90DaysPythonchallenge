from  datetime import datetime #an import statement to import the datetime module

name = str(input("Enter your name: ")) #name is a string 
age = int(input("Enter your age: ")) #age is an integer
current_year = datetime.now().year #current_year is an integer
birth_year = current_year - age #birth_year is an integer
# Print the greeting and birth year
print(f"Hello {name}! You were born in {birth_year}.")