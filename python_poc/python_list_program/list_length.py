from operator import length_hint


def naive_method():
    list_container = [1,2,3,4,5]
    count = 0
    for i in list_container:
        count = count+1
    print(count)


def len_method():
    list_container = [1, 2, 3, 4, 5]
    print(len(list_container))


def len_hint_method():
    list_container = [1, 2, 3, 4, 5]
    print(length_hint(list_container))


naive_method()
len_method()
len_hint_method()
