def naive_method():
    list_container = [2,5,1,7,4,8,3,9]
    first_max = list_container[0]
    second_max = 0
    for i in range(len(list_container)):
        if first_max < list_container[i]:
            second_max = first_max
            first_max = list_container[i]

    print("seconf largest number in arrya {} is  : {}".format(list_container,second_max))

def sort_method():
    list_container = [2, 5, 1, 7, 4, 8, 3, 9]
    print("araay : ",list_container)
    list_container.sort()
    print("seconf largest number is : ",list_container[len(list_container)-2])


def max_remove():
    list_container = [2, 5, 1, 7, 4, 8, 3, 9]
    print("araay : ", list_container)
    list_container.pop()
    print(list_container)

    list_container.remove(max(list_container))
    second_largest = max(list_container)

    print("seconf largest number is : ", second_largest)

naive_method()
sort_method()
max_remove()