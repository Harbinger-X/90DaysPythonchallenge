#This project helps us to learn about json,how to create and parse json files using python library 
import json

import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file!")
        return None

def search_json(data):
    while True:
        print("\n=== JSON Data Search ===")
        print("Available keys:", ", ".join(data.keys()))
        
        key = input("\nEnter a key to search (or 'quit' to exit): ")
        
        if key.lower() == 'quit':
            print("Goodbye!")
            break
            
        if key in data:
            print(f"\nValue for '{key}':")
            print(data[key])
        else:
            print(f"Key '{key}' not found!")

# Main program
filename = input("Enter the JSON file name: ")
data = read_json_file(filename)

if data:
    search_json(data)