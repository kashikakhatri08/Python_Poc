from itertools import chain


def naive_method():
    dict_container = {1:4,2:5,3:6}
    list_container=[]
    for i in dict_container:
        list_container.append(i)
    for i in dict_container.values():
        list_container.append(i)
    print(list_container)


def list_method():
    dict_container = {1: 4, 2: 5, 3: 6}
    res_list = list(dict_container.keys())+list(dict_container.values())
    print(res_list)


def chain_method():
    dict_container = {1: 4, 2: 5, 3: 6}
    res_list = list(chain(dict_container.keys(),dict_container.values()))
    print(res_list)


naive_method()
list_method()
chain_method()

