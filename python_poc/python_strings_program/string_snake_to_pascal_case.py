# snake case = hello_there
# pascal case = HelloThere
import string


def naive_string_converstion():
    string_container = "naive_string_converstion"
    string_split = string_container.split("_")
    count = 0
    string_res = ""
    for i in range(len(string_split)):
        for j in str(string_split[i]):
            if count == 0:
                string_res = string_res + j.capitalize()
                count = count + 1
            else:
                string_res = string_res + j
        count = 0
    print(string_res)


def title_replace_converstion():
    string_container = "title_replace_converstion"
    string_res = string_container.replace("_", " ").title().replace(" ", "")
    print(string_res)


def string_capword_converstion():
    string_container = "string_capword_converstion"
    string_res = string.capwords(string_container.replace("_", " ")).replace(" ", "")
    print(string_res)


naive_string_converstion()
title_replace_converstion()
string_capword_converstion()
