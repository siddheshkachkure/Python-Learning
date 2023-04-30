li = []
def function():
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num):
        a=int(input())
        li.append(a)
    print(li)
def newlis():
    global li
    first = li[0]
    last = li[len(li)-1]
    var = [first,last]
    print(var)

function()
newlis()