# A simple script that reads a file and counts the number of lines and words in the file
with open('example.txt', "r") as file: # Open the file in read mode
    lines = file.readlines()  # Read all lines

    line_count = len(lines)  # Count the number of lines

    word_count = sum(len(line.split()) for line in lines)# Count the number of words

    # Print the results
    print(f"Total Lines: {line_count}")
    print(f"Total Words: {word_count}")