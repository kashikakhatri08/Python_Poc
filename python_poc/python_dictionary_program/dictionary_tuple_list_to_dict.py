def naive_method():
    list_container = [("kashika",10),("john",20),("anne",30)]
    dict = {}
    for i in list_container:
        dict[i[0]] = [i[1]]


    print(dict)

def set_default_method():
    list_container = [("kashika", 10), ("john", 20), ("anne", 30)]
    dict_set = {}
    for i,b in list_container:
        dict_set.setdefault(i,[]).append(b)
    print(dict_set)


naive_method()
set_default_method()