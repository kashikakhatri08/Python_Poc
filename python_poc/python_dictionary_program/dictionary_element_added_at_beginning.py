from collections import OrderedDict


def naive_method():
    dict_container = {1:10,2:20}
    add_item = {3:30,4:40}
    dict_container = OrderedDict(dict_container)
    add_item = OrderedDict(add_item)
    print(dict(dict_container))
    for i in dict_container:
        add_item[i]=dict_container[i]

    dict_container = add_item
    print(dict(dict_container))

def Move_to_end_method():
    dict_container = {1: 10, 2: 20}
    add_item = {3: 30}

    dict_container = OrderedDict(dict_container)
    dict_container.update(add_item)
    dict_container.move_to_end(3,last = False)
    print(dict(dict_container))


def add_operator_method():
    dict_container = {1: 10, 2: 20}
    add_item = {3: 30, 4: 40}
    dict_container = OrderedDict(dict_container)
    add_item = OrderedDict(add_item)
    res_dict = OrderedDict(list(add_item.items())+list(dict_container.items()))
    print(dict(res_dict))




naive_method()
Move_to_end_method()
add_operator_method()