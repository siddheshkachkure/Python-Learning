def div():
    number=int(input("Enter the number:: "))
    my_empty_list=[]
    for num in list(range(1,number+1)):
        if number%num==0:
            my_empty_list.append(num)

    print("Divisors are",my_empty_list)
div()