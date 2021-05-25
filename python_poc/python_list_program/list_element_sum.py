def naive_method():
    list_container = [1,2,3,4,5]
    sum = 0
    for i in range(len(list_container)):
        sum += list_container[i]
    print(sum)


def while_loop():
    list_container = [1,2,3,4,5]
    sum = 0
    i=0
    while i <len(list_container):
        sum += list_container[i]
        i = i+1
    print(sum)


def recursive(list_container,size):
    if size == 0:
        return 0
    else:
        list_sum = list_container[size -1]+recursive(list_container,size-1)
        return list_sum


def sum_method():
    list_container = [1, 2, 3, 4, 5]
    list_sum=sum(list_container)
    print(list_sum)


def main():
    naive_method()
    while_loop()
    list_container = [1, 2, 3, 4, 5]
    size = len(list_container)
    sum = recursive(list_container,size)
    print(sum)
    sum_method()

main()