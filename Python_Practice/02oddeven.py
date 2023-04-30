num = int(input("Enter any number:: "))

def oddeven(number):
    if number % 2 == 0 and number % 4 != 0:
        print(f"The number {number} is even.")
    elif number % 2 == 0 and number % 4 == 0:
        print(f"The number {number} is even and is divisible by 4.")
    else:
        print(f"The number {number} is odd and also not divisible by multiple of 2")

oddeven(num)