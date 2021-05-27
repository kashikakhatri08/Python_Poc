from itertools import permutations



def native_method():
    string_container = "123"
    str_com = permutations(string_container)
    for i in list(str_com):
        str_per = "".join(i)
        print(str_per)

native_method()
