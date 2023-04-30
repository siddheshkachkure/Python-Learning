
a = int(input('Enter 1st Number:: '))
b = int(input('Enter 2nd Number:: '))
c = int(input('Enter 3rd Number:: '))

def GretterNo(a,b,c):

    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
        return b
    elif c>a&b:
        return c
print("Grettest Number is",GretterNo(a,b,c))
GretterNo(a,b,c)

#while True:
#menu()
    
    