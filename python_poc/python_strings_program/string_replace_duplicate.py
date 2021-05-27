def dict_enumerate():
    string_container = "Gfg is best . Gfg also has Classes now. Classes help understand better ."
    dict_replace = {"Gfg": "It" , "Classes": "They"}
    string_split =string_container.split()
    res_set = set()
    for elem1 , elem2 in enumerate(string_split):
        if elem2 in dict_replace:

            if elem2 in res_set:

                string_split[elem1] = dict_replace[elem2]

            else:
                res_set.add(elem2)


    res_set = " ".join(string_split)
    print(res_set)


def dict_index():
    string_container = "Gfg is best . Gfg also has Classes now. Classes help understand better ."
    dict_replace = {"Gfg": "It", "Classes": "They"}
    string_split = string_container.split()
    res_set = " ".join(dict_replace.get(val2) if val2 in dict_replace.keys() and string_split.index(val2) != val1
                      else val2 for val1, val2 in enumerate(string_split))

    print(res_set)
dict_enumerate()
dict_index()