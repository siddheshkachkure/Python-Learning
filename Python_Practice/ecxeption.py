
# my custom exception created 
class negative_number_error(Exception):
    pass

#1) Create a postive numbered list 
#Note : raise an exception if the users inserts a negative number OR user creates an empty list 
def create_positive_numbered_list():
    my_list=[]
    num = int(input("Please enter a number to be added "))
    for cntr in range(0,int(input("Please enter number of elements to the numbered list"))):
        if num <0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

def create_negative_numbered_list():
    my_list=[]
    num = int(input("Please enter a number to be added "))
    for cntr in range(0,int(input("Please enter number of elements to the numbered list"))):
        if num >=0:
            raise  negative_number_error
        else:
            my_list.append(num)
    print(my_list)   

# invocation
try:
    create_positive_numbered_list()        
except negative_number_error:     
    print("I handled negative_number_error exception")