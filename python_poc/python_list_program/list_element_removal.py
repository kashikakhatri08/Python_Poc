def remove_even_1():
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list_container:
        if i % 2 == 0:
            list_container.remove(i)
    print(list_container)


def remove_even_2():
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_odd = [i for i in list_container if i % 2 != 0]
    print(list_odd)


def remove_given_elements():
    list_removal = []
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    remove_elements = [0, 1, 8, 9]
    for i in list_container:
        for j in remove_elements:
            if i == j:
                list_removal.append(i)

    for i in range(len(list_removal)):
        list_container.remove(list_removal[i])

    print(list_container)


def remove_given_index_1():
    list_removal = []
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    remove_elements = [0, 1, 3, 5]
    for i in range(len(list_container)):
        for j in remove_elements:
            if i == j:
                list_removal.append(list_container[i])

    for i in range(len(list_removal)):
        list_container.remove(list_removal[i])

    print(list_container)


def remove_given_index_2():
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    removal_index = [0, 5, 9]
    for i in sorted(removal_index, reverse=True):
        del list_container[i]
    print(list_container)
    """
        difference between the list sort() function and the sorted() function is that the sort() function will 
        modify the list it is called on. The sorted() function will create a new list 
        containing a sorted version of the list it is given.
        """


def slicing_remove():
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del list_container[1:5]
    print(list_container)


def list_comperhison():
    list_container = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    removal_element = [8, 3, 5]
    list_removed = [i for i in list_container if i not in removal_element]
    print(list_removed)


remove_even_1()
remove_even_2()
remove_given_elements()
remove_given_index_1()
remove_given_index_2()
slicing_remove()
list_comperhison()
