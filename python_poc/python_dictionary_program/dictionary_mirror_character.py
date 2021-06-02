import string


def naive_method():
    string_container = "paradox"
    num = 3
    string_first =string_container[0:num]
    string_sec = string_container[num:]
    alpha_first = string.ascii_lowercase[0:13]
    alpha_sec = string.ascii_lowercase[26:13-1:-1]


    for i in range(0, len(string_sec)):
        #val = alphabat.find(string_container[i])
        if string_sec[i] in alpha_sec:
            number = alpha_sec.find(string_sec[i])
            string_sec = string_sec.replace(string_sec[i], alpha_first[number])
        elif string_sec[i] in alpha_first:
            number = alpha_first.find(string_sec[i])
            string_sec = string_sec.replace(string_sec[i], alpha_sec[number])
    print("mirror string of string '{}' is '{}'".format(string_container,string_first+string_sec))


def zip_method():
    string_container = "paradox"
    num = 3
    string_first = string_container[0:num]
    string_sec = string_container[num:]
    alpha_str = string.ascii_lowercase[:]
    alpha_rev = string.ascii_lowercase[::-1]
    dict_container = dict(zip(alpha_str,alpha_rev))
    Mirror_result = ""
    for i in range(0, len(string_sec)):
        Mirror_result += dict_container[string_sec[i]]


    print("mirror string of string '{}' is '{}'".format(string_container, string_first + Mirror_result))


naive_method()
zip_method()
