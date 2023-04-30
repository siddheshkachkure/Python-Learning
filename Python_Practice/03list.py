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
    n = int(input("Enter the Range:: "))
    my_new_list = []
    for x in a:
        if x <= n:
            my_new_list.append(x)
    print("lessthan values",my_new_list)
        
function()
area()
