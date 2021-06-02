from collections import Counter


def naive_method():
    string_container = "aabcd"
    dict_count = dict(Counter(string_container))

    list_value =list(set(dict_count.values()))

    if len(list_value) > 2:
        print("no")
    elif len(list_value) == 2 and list_value[1]-list_value[0]>1:
        print("no")
    else:
        print("yes")



naive_method()