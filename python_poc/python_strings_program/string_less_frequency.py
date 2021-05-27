from collections import Counter


def naive_method():
    string_container = "kashikakhatri"
    dict_string = {}

    for i in str(string_container):
        if i in dict_string:
            dict_string[i] += 1
        else:
            dict_string[i] = 1

    count= min(dict_string,key =dict_string.get)
    print(count)

def counter_method():
    string_container = "kashikakhatri"
    counter_dict = Counter(string_container)

    count= min(counter_dict,key =counter_dict.get)
    print(count)
naive_method()
counter_method()