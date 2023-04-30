my_dict = {}
def menu():
    print("\t------------------------MENU------------------------")
    print("1. Make a Dictionary of  'Country' :: Capital Relationship ")
    print("2. Add New Country in the Dictionary")
    print("3. Remove Country from the Dictionary")
    print("4. Exit ")

def fun1():

    n=int(input("Enter the number of Countries you want to input: "))
    i=0
    for i in range(0,n,1):
        country = input("Enter Country name: ")
        capital = input("Enter Capital name: ")
        my_dict[country]=capital
    print(my_dict)

def fun3():
    country=[]
    capital=[]
    for key,value in zip(country,capital):
        my_dict[key]=value
    print(my_dict)

def fun2():
    print(my_dict)
    country = input("Enter key name: ")
    del my_dict[country]
    print(my_dict)








