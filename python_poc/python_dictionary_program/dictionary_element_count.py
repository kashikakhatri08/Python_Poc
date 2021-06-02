from collections import Counter


def naive_method():
    list_container = ["a", "b", "c"
        , "b", "b", "c"
        , "a", "b", "a"
        , "c", "a", "a"]
    dict_container = {}
    for i in list_container:
        dict_container[i] = list_container.count(i)

    max = 0
    string_max = ""
    for i, j in dict_container.items():
        if j > max:
            max = j
            string_max = i
    print(list_container)
    print(dict_container)
    print("{} have the maximum vote : {} ".format(string_max, max))


def counter_method():
    list_container = ["a", "b", "c"
        , "b", "b", "c"
        , "a", "b", "a"
        , "c", "a", "a"]
    dict_container = {}
    counter_dict = Counter(list_container)
    for i in counter_dict.values():
        dict_container[i] = []
    for key, value in counter_dict.items():
        dict_container[value] = key
    max_vote = sorted(dict_container.keys(), reverse=True)[0]
    if max_vote > 1:
        print("{} have the maximum vote : {} ".format(sorted(dict_container[max_vote])[0], max))
    else:
        print(dict_container[max_vote])


def max_method():
    list_container = ["a", "b", "c"
        , "b", "b", "c"
        , "a", "b", "a"
        , "c", "a", "a"]

    counter_dict = Counter(list_container)
    max_number = max(counter_dict.values())
    result = [i for i in counter_dict.keys() if counter_dict.get(i) == max_number]
    print("{} have the maximum vote  ".format(result[0]))


naive_method()
counter_method()
max_method()
