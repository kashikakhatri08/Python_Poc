def naive_method():
    list_container = [6,5,2,4,3]
    list_min = list_container[0]
    for i in range(len(list_container)):
        if list_min > list_container[i]:
            list_min = list_container[i]
    print(list_min)


def sorted_method():
    list_container = [6,5,2,4,3]
    list_container.sort()

    list_min = list_container[0]
    print(list_min)


def min_methodd():
    list_container = [6,5,2,4,3]
    list_min=min(list_container)
    print(list_min)


naive_method()
sorted_method()
min_methodd()


