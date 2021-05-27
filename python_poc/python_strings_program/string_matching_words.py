import re


def naive_method():
    string_container_1 = "abcdef"
    string_container_2 = "deavhdi"
    string_format = ""

    for i in string_container_1:

        for j in string_container_2:

            if i == j:

                if i not in string_format:
                    string_format = string_format + " " + i

    print(string_format)
    print(len(string_format.replace(" ","")))

def set_method():
    string_container_1 = "abcdef"
    string_container_2 = "deavhdi"
    set_container_1 = set(string_container_1)
    set_container_2 = set(string_container_2)
    count = set_container_1 & set_container_2
    print(count)

def regular_expression():
    string_container_1 = "abcdef"
    string_container_2 = "deavhdi"
    count = 0
    for i in string_container_1:
        if re.search(i,string_container_2):
            count += 1

    print(count)


naive_method()
set_method()
regular_expression()
