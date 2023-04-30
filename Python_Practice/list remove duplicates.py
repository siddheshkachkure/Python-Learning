#-----------------------------------Using Sets-------------------------

li = []
def function():
    num=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,num):
        a=int(input())
        li.append(a)
    print(li)
    print("List a = ", li)
    sam_set = set()
    for items in li:
        sam_set.add(items)
        Set = sam_set
    print(list(Set))

