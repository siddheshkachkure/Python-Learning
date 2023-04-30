
class Error(Exception):
    pass
class Small(Error):
    pass
class Large(Error):
    pass

number = 5

while True:
    try:
        num = int(input("Enter a number in Range(0-10):: "))
        if num < number:
            raise Small
        elif num > number:
            raise Large
        else:
            print("Congratulations! You guessed it correctly.")
        break
    except Small:
        print("This value is too small, try again!")
    except Large:
        print("This value is too large, try again!")

    if input("\n" "Do you want to play again? (Y/N): ") == "N":
        break