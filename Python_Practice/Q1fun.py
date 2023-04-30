def popul():
    m_list=[]
    n=int(input("Enter Number of Members you want to add in the list  :: "))
    i=0
    for i in range(0,n):
        a=str(input())
        m_list.append(a)
        
    def mem_list():
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("Listed Members are :: ",m_list)
    mem_list()
    def app():
        print("Enter new Member :: ")
        a=str(input())
        m_list.append(a)
        print(m_list)
    app()
    def appv():
        n=int(input("Enter Number of Members you want to add in the list  :: "))
        i=0
        for i in range(0,n):
            a=str(input())
            m_list.append(a)
        print("Updated List :: ",m_list)
    appv()
    def rm():
        k=int(input("For Deletion input index Number::"))
        m_list.pop(k)
        print(m_list)
    rm()
popul()