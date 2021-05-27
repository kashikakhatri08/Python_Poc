def remove_string():
    string_container = "kashika"
    n = 2
    for i in range(len(string_container)):

        if i == n:
            string_container = string_container.replace(string_container[i], "")
    print(string_container)


def divide_merge():
    string_container = "kashika"
    n = 2
    string_1 = string_container[:n]
    string_2 = string_container[n + 1:]
    string_merged = string_1 + string_2
    print(string_merged)


remove_string()
divide_merge()
