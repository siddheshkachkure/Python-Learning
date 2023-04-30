# YOU CAN USE this program with :: str p type also for pythonic approach 
from datetime import date
today=date.today()
print("TODAY`S DATE :: ",today)

# tlist=[]
# list=[]

print("Enter Todays Date When Prompted as in the format asked :: ")
print("------------------------------------------------")
a1=int(input("Enter DATE  as DD:: "))
b1=int(input("Enter MONTH as MM ::"))
c1=int(input("Enter YEAR as YYYY :: "))
# tlist.append(c1)
# tlist.append(b1)
# tlist.append(a1)

print("Enter DOB When Prompted as in the format asked :: ")
print("------------------------------------------------")
a=int(input("Enter DATE  as DD:: "))
b=int(input("Enter MONTH as MM ::"))
c=int(input("Enter YEAR as YYYY :: "))
# list.append(c)
# list.append(b)
# list.append(a)

a2=a-a1
x=abs(a2)
b2=b-b1
y=abs(b2)
c2=c-c1
z=abs(c2)
print("Your Age is :: ",z,"years",y,"months",x,"days")


# print(tlist)
# print(list)
# A=set(tlist)
# B=set(list)
# print (A)
# print(B)
# age = int((date.today() - list).days)
# print (age)
