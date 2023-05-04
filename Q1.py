""" Wrte a code snippet that should ask the user to enter a string and display the characters that are repeated in a list 
"""

string = input("Enter a string: ")

repeated_chars = []

for char in set(string):
    if string.count(char) > 1:
        repeated_chars.append(char)

print("The repeated characters are:", repeated_chars)
