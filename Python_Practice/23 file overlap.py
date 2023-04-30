def prime():
    with open('primenumbers.txt', 'r') as open_prime:
        opened = list(open_prime.read().split("\n"))
    return opened

def happy():
    with open('happynumbers.txt', 'r') as open_happy:
        opened = list(open_happy.read().split("\n"))
        return opened
        my_list = [x for x in return_prime() if x in return_happy()]
        print(my_list)