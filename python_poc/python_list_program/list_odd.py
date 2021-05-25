def for_loop():
    list_container = [2,5,6,8,9]
    odd_list = []
    for i in range(len(list_container)):
        if list_container[i] % 2 != 0:
            odd_list.append(list_container[i])

    print(odd_list)

def while_loop():
    list_container = [2, 5, 6, 8, 9]
    odd_list = []
    i =0
    while i < len(list_container):
        if list_container[i] % 2 != 0:
            odd_list.append(list_container[i])
        i =i +1

    print(odd_list)

def list_comprehension():
    list_container = [2, 5, 6, 8, 9]
    list_odd= [ num for num in list_container if num % 2 == 1]
    print(list_odd)

def lambda_method():
    list_container = [2, 5, 6, 8, 9]
    list_odd = list(filter(lambda x: (x%2 != 0),list_container))
    #The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    print(list_odd)


for_loop()
while_loop()
list_comprehension()
lambda_method()

