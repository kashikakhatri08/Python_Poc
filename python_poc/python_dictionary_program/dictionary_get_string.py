from collections import Counter


def naive_method():
    string_1 = "kashikakHAtri"
    string_2 = "wkyarstgbhcvidfgkfgbaedfgktghnhedfbnasdfghjtefgbrdfvbnI"
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    dict_1 = dict(Counter(string_1))
    dict_2 = dict(Counter(string_2))
    count = 0
    for i,j in dict_1.items():
        if i in dict_2.keys():
           if j <= dict_2[i]:
               count = count +1
    if count == len(dict_1):
        print("possible")
    else:
        print("not possible")
def intrsection_method():
    string_1 = "kashikakHAtri"
    string_2 = "wkyarstgbhcvidfgkfgbaedfgktghnhedfbnasdfghjtefgbrdfvbnI"
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    dict_1 = dict(Counter(string_1))
    dict_2 = dict(Counter(string_2))
    result = dict_1.intersection(dict_2)
    if result == dict_1:
        print("possible")
    else:
        print("not possible")



naive_method()
intrsection_method()