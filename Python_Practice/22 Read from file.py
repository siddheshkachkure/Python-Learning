# print(r"At classmate \n we are commited")
# with open('22_Read_file.txt', 'r') as open_file:
#    line = open_file.read()
# while line:
#    print(line)
#    line = open_file.read()

# file1 = open("22_Read_file.txt", "w")
# L = ["This is Delhi"]
# file1.write(L)


# file1 = open("22_Read_file.txt", "a")  # append mode
# file1.write("Today \n")
# file1.close()


file1 = open('22_Read_file.txt', 'w+')
#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "hey\n"
file1.write(s)
#file1.writelines(L)
file1.close()
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()

