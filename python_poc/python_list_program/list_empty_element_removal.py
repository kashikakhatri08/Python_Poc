def list_comprehension():
    list_container = [1, 5, [], 8, 9, [], []]
    new_list = [list_ele for list_ele in list_container if list_ele != []]
    print(new_list)


def filter_method():
    list_container = [1, 5, [], 8, 9, [], []]
    new_list = list(filter(None, list_container))
    print(new_list)
    """
    filter syntax:-
    filter(function, iterable)
    With filter function as None, the function defaults to Identity
    function, and each element in random_list is checked if it's true or not.
    will return a list for not None values
    """

list_comprehension()
filter_method()
