from collections import Counter


def naive_method():
    string_container = "kashika"
    dict = {}
    for i in string_container:
        dict[i] = string_container.count(i)

    for i in dict:
        if dict.get(i) > 1:
            print("letter {} is repeatable".format(i))


def counter_method():
    string_container = "kashika"
    dict_string = Counter(string_container)

    for i in dict_string:
        if dict_string.get(i) > 1:
            print("letter {} is repeatable".format(i))


naive_method()
counter_method()





