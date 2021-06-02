def naive_method():
    dict_container = {1: 12, 2: 23, 3: 34, 4: 45}
    key = 3
    del dict_container[key]

    print(dict_container)


def pop_method():
    dict_container = {1: 12, 2: 23, 3: 34, 4: 45}
    key = 3
    remove_val = dict_container.pop(key)
    print(remove_val)
    remove_not_exisiting = dict_container.pop(5, 56)  # no exception
    print(remove_not_exisiting)
    print(dict_container)


def dict_comprehension():
    dict_container = {1: 12, 2: 23, 3: 34, 4: 45}
    key = 3
    dict_res = {keys: val for keys, val in dict_container.items() if keys != key}
    print(dict_res)


naive_method()
pop_method()
