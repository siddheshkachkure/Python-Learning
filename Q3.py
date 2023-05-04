""" Write a code snippet that should accept input in form of key value to store the following details.
{
"username" : "abc"
"age" : "27"
"salary" : "17000.89"
"status" : "true"
"department" : ["ACTS", "HPC"]
}
"""

details = {}

details["username"] = input("Enter username: ")
details["age"] = input("Enter age: ")
details["salary"] = input("Enter salary: ")
details["status"] = input("Enter status: ")
details["department"] = input("Enter department (comma-separated): ").split(",")

print("Details stored:", details)

