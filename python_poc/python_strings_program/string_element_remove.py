def ele_remove():
    string_container = "kashika"
    string_new = ""
    n = 3
    for i in range(0,len(string_container)):
        if i != n:
            string_new = string_new + string_container[i]
    print(string_new)


def replace_method():
    string_container = "kashika"
    string_new = string_container.replace("h",'')
    print(string_new)


def slicing_method():
    string_container = "kashika"
    n = 3
    string_new = string_container[:n-1] + string_container[n:len(string_container)]
    print(string_new)


def join_method():
    string_container = "kashika"
    n = "h"
    string_new = ''.join(i for i in string_container if i != n)
    print(string_new)


ele_remove()
replace_method()
slicing_method()
join_method()
