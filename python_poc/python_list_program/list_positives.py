def for_loop():
    list_container = [1,-3,9,5,-6,0]
    for i in range(len(list_container)):
        if list_container[i] >= 0:
            print(list_container[i])


def while_loop():
    list_container = [1, -3, 9, 5, -6, 0]
    i=0
    while i < len(list_container):
        if list_container[i] >= 0:
            print(list_container[i])
        i = i+1


def list_comprehension():
    list_container = [1, -3, 9, 5, -6, 0]
    list_positives = [i for i in list_container if i >=0 ]
    print(list_positives)



def lambda_expression():
    list_container = [1, -3, 9, 5, -6, 0]
    list_positives = list(filter(lambda x :( x>=0 ) ,list_container))
    print(list_positives)


for_loop()
while_loop()
list_comprehension()
lambda_expression()