def naive_method():
    list_container = [6,5,2,4,3]
    list_max = list_container[0]
    for i in range(len(list_container)):
        if list_max < list_container[i]:
            list_max = list_container[i]
    print(list_max)


def sorted_method():
    list_container = [6,5,2,4,3]
    list_container.sort()

    list_max = list_container[len(list_container)-1]
    print(list_max)


def max_methodd():
    list_container = [6,5,2,4,3]
    list_max=max(list_container)
    print(list_max)


naive_method()
sorted_method()
max_methodd()


