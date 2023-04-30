m_list=[]

def member():
    n=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,n):
        a=str(input())
        m_list.append(a)
           
def length():
    print("Total No of Members in the list are :: ",len(m_list))

def mem_list(): 
    print("Listed Members are :: ",m_list)

def app():
    print("Enter new Member :: ")
    a=str(input())
    m_list.append(a)
    print(m_list)
    
def appv():
    n=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,n):
        a=str(input())
        m_list.append(a)
    print("Updated List :: ",m_list)

def rm():
    k=int(input("For Deletion input index Number::"))
    m_list.pop(k)
    print(m_list)
    
def rmv():
    del m_list[-1]
    print(m_list)
    
def dis():
    p=int(input("Enter index Number to Show Details ::  "))
    print("Details of ",p,"are :: ",m_list[p])