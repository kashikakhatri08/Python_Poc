import copy


def slicing_method():
    list_container = [1,2,3,4,5,6,7,8]
    list_copy = list_container[:]
    print(list_copy)


def extend_method():
    list_container = [1, 2, 3, 4, 5, 6, 7, 8]
    list_copy = []
    list_copy.extend(list_container)
    print(list_copy)


def list_method():
    list_container = [1,2,3,4,5,6,7,8]
    list_copy = list(list_container)
    print(list_copy)


def list_comprehenson():
    list_container = [1, 2, 3, 4, 5, 6, 7, 8]
    list_copy = [i for i in list_container]
    print(list_copy)


def list_append():
    list_container = [1, 2, 3, 4, 5, 6, 7, 8]
    list_copy = []
    for i in list_container:
        list_copy.append(i)
    print(list_copy)

def copy_method():
    list_container = [1, 2, 3, 4, 5, 6, 7, 8]
    list_copy = list_container.copy()
    print(list_copy)

def shallow_copy():
    list_container = [1, 2, [3, 4], 5, 6, 7, 8]
    print("original copy",list_container)
    list_copy = copy.copy(list_container)
    #or list_copy = list(list_container)
    print("shallow copy list print",list_copy)
    list_container[2][0]= 0
    print("shallow copy list after change in original list", list_copy)
    list_copy[2][0]= 3
    print("original list after change in shallow copied list", list_container)


def deep_copy():
    list_container = [1, 2, [3, 4], 5, 6, 7, 8]
    print("original copy", list_container)
    list_copy = copy.deepcopy(list_container)
    print("deep copy list print", list_copy)
    list_container[2][0] = 0
    print("cdeep opy list after change in original list", list_copy)
    list_copy[2][0] = 3
    print("original list after change in deep copied list", list_container)





#for understanding shallow and deep refer
#https://realpython.com/copying-python-objects/#:~:text=A%20shallow%20copy%20means%20constructing,of%20the%20child%20objects%20themselves.

slicing_method()
extend_method()
list_method()
list_comprehenson()
list_append()
copy_method()
shallow_copy()
deep_copy()