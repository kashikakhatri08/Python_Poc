import re


def substring_persent():
    string_container_1 = "hello"
    string_container_2 = "hello is there"
    string_container_2_words = string_container_2.split(" ")
    for i in range(len(string_container_2_words)):
        if string_container_1 == string_container_2_words[i]:
            print("{} is persent in {} string".format(string_container_1, string_container_2))
            break
        else:
            print("{} is not persent in {} string ".format(string_container_1, string_container_2))


def find_method():
    string_container_1 = "hello"
    string_container_2 = "hello is there"
    string_search = string_container_2.find(string_container_1)

    if (string_search == -1):
        print("{} is not persent in {} string".format(string_container_1, string_container_2))
    else:
        print("{} is  persent in {} string ".format(string_container_1, string_container_2))


def count_method():
    string_container_1 = "hello"
    string_container_2 = "hello is there"
    string_search = string_container_2.count(string_container_1)
    if (string_search > 0):
        print("{} is  persent in {} string".format(string_container_1, string_container_2))
    else:
        print("{} is  not persent in {} string ".format(string_container_1, string_container_2))


def regular_expression():
    string_container_1 = "hello"
    string_container_2 = "hello is there"

    if (re.search(string_container_1, string_container_2)):
        print("{} is  persent in {} string".format(string_container_1, string_container_2))
    else:
        print("{} is  not persent in {} string ".format(string_container_1, string_container_2))


substring_persent()
find_method()
count_method()
regular_expression()
