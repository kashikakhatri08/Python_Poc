from collections import Counter


def naive_method():
    list_container_1 = ["hi","hello","bye"]
    list_container_2 = ["h","l","o","i","e"]
    dict_container =dict(Counter(list_container_1))
    flag = False
    print(dict_container)

    for i in dict_container:
        string_make = ""
        for j in str(i):
            if j in list_container_2:
                string_make += j

        if string_make == i:
            print("using list of words {} we can make word '{}'".format(list_container_2,i))
        else:
            print("using list of words {} we can't make word '{}'".format(list_container_2, i))

naive_method()