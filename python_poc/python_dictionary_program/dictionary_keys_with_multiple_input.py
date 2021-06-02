def random_input_method():
    dict_container = {}
    x,y,z = 1,2,3
    dict_container[x,y,z] = x+y -z
    print(dict_container)
    x, y, z = 5,2,2
    dict_container[x, y, z] = x + y - z
    print(dict_container)

def list_as_keys():
    dict_container = {(1,2):"a" ,(4,5):"b"}
    first = []
    second = []
    val = []
    for i in dict_container:
        first.append(i[0])
        second.append(i[1])
        val.append((dict_container[(i[0],i[1])]))

    print(first,second,val)




random_input_method()
list_as_keys()
