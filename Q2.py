""" Write a code snippet that should ask the user to enter the number starting from 1 to 10. 
Choose the data structure in such a way that should not allow any kind of append and assignement of values later.
"""


num = int(input("Enter a number between 1 and 10: "))
if num < 1 or num > 10:
    print("Invalid input.")
else:
    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("The value at index", num-1, "is", values[num-1])
