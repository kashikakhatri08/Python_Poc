from collections import Counter


def naive_method():
    list_container = [1,2,3,1,4,2,2,5,4,3,4,5,3]
    dict_res = dict(Counter(list_container))
    print(dict_res)

naive_method()
