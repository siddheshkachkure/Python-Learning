li = []
def function():
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num+1):
        a=int(input())
        li.append(a)
    print("Entered list:",li)
    print("Even list:",[i for i in li if i%2 == 0])

function()