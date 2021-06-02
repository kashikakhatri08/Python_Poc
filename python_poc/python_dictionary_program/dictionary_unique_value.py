from itertools import chain


def naive_method():
    dict_container = {"abc": [5, 6, 7, 8], "efg": [1, 2, 3, 4], "hik": [9, 10]}
    list_res = []
    for i in dict_container.values():
        for j in i:
            list_res.append(j)

    list_res.sort()
    print(list_res)


def chain_method():
    dict_container = {"abc": [5, 6, 7, 8], "efg": [1, 2, 3, 4], "hik": [9, 10]}
    list_res = list(sorted(chain(*dict_container.values())))
    print(list_res)

    """
    chain()
    It is a function that takes a series of iterables and returns one iterable. 
    It groups all the iterables together and produces a single iterable as output.
    Syntax : 
    chain (*iterables)
    https://www.geeksforgeeks.org/python-itertools-chain/
    """


naive_method()
chain_method()
