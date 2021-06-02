from collections import OrderedDict, Counter


def naive_method():
    list_container = ["ant", "magenta", "magnate", "tan", "gnamate"]
    sorted_string = " "
    dict = {}
    for i in list_container:
        sorted_string += "".join(sorted(i)) + " "
    for i in sorted_string.split(" "):
        if i != "":
            if i in dict.keys():
                dict[i] = dict.get(i) + 1
            else:
                dict[i] = 1
    value = max(dict.values())
    for i in dict:
        if dict.get(i) == value:
            get_key = i

    print("letter combination {} have {} anagram in list : {}".format(get_key, value, list_container))


def counter_method():
    string_container = "ant magenta magnate tan gnamate"

    string_container = string_container.split(" ")

    for i in range(0, len(string_container)):
        string_container[i] = "".join(sorted(string_container[i]))
    dict = Counter(string_container)
    value = max(dict.values())
    for i in dict:
        if dict.get(i) == value:
            get_key = i

    print("letter combination {} have {} anagram in list : {}".format(get_key, value, string_container))


naive_method()
counter_method()
