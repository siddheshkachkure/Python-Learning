'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches'''
height = float(input("Enter the height in cms:"))
new_height = height*0.393701
print("The height in inches is:",new_height)
height_in_feet = new_height/12
print("The height in feet is:",height_in_feet)