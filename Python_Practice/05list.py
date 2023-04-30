my_list = []
my_second_list = []
def function():
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num):
        a=int(input())
        my_list.append(a)
    print(my_list)

def function2():
    global my_second_list
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num):
        a=int(input())
        my_second_list.append(my_second_list)
    print(my_second_list)

A = set(my_list)

B = set(my_second_list)

C = set(A&B)

C = A.union(B)

print(list(C))

function()
function2()