def sorted_method():
    dict_container = {1: "b", 6: "a", 3: "g", 4: "f"}
    # sorted by keys
    for i in sorted(dict_container.keys()):
        print("{} : {}".format(i, dict_container[i]))
    # sorted by value
    res_1 = sorted(dict_container.items(), key=lambda x: (x[1], x[0]))
    print(res_1)
    # sorted by key
    res_2 = sorted(dict_container.items())#:it will sort in lexicogrphical()change alpha into binaery order Taking key’s type as string
    print(res_2)


sorted_method()
