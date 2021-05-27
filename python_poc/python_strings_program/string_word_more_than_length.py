def naive_method():
    string_container = "Hello my name is kashika khatri"
    n = 4
    list_string = []
    string_split = string_container.split()
    for i in range(len(string_split)):
        if len(string_split[i]) > n:
            list_string.append(string_split[i])
    print(list_string)

naive_method()
