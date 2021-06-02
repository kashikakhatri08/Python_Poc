def naive_method():
    dict_container = {1: 100, 2: 200, 3: 300}
    sum_dict = 0
    for i in dict_container.values():
        sum_dict += i
    print(sum_dict)


naive_method()
