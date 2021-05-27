def naive_print():
    string_container = "how are you , hola"
    string_split = string_container.split()
    for i in range(len(string_split)):
        if len(string_split[i]) % 2 == 0:
            print(string_split[i])

naive_print()