my_list = []

def function():
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num):
        a=int(input())
        my_list.append(a)
    print(my_list)

def area():
    a =my_list
    n = int(input("Enter the number that you want to search:: "))
    my_new_list = []
    for x in a:
        if x <= n:
            my_new_list.append(x)
    print("my list",my_new_list)
    if n in my_new_list:
        print("The number is present in the list:: ",n)
    else:
        print("The number is not present in the list!!")

function()
area()