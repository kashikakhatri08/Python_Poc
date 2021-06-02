def sorted_method():
    dict_container = {"a": [1, 3, 2], "c": [6, 4, 5], "b": [8, 7, 9]}
    res = dict()
    for i in sorted(dict_container):
        res[i] = sorted(dict_container.get(i))

    print(res)


def dict_comprenshion():
    dict_container = {"a": [1, 3, 2], "c": [6, 4, 5], "b": [8, 7, 9]}
    res = {key: sorted(dict_container.get(key)) for key in sorted(dict_container)}
    print(res)


sorted_method()
dict_comprenshion()
