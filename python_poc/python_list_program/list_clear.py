def clear_method():
    list_container =[1,2,3,4,5]
    print(list_container)
    print(list_container.clear()) #None
    print(list_container)

def empty_list_assign():
    list_container = [1, 2, 3, 4, 5]
    print(list_container)
    list_container = []
    print(list_container)


def multiply_with_zero():
    list_container = [1, 2, 3, 4, 5]
    print(list_container)
    list_container *= 0
    print(list_container)

def del_method():
    list_container = [1, 2, 3, 4, 5]
    print(list_container)
    del list_container
    #print(list_container)
    """
     File "/home/kakh272961/PycharmProjects/pythonoc/python_list_program/list_clear.py", line 24, in del_method
    print(list_container)
UnboundLocalError: local variable 'list_container' referenced before assignment
    """


clear_method()
empty_list_assign()
multiply_with_zero()
del_method()
