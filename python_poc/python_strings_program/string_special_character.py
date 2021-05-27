import re


def native_method():
    string_container = "kas@hika$kha#tri"
    flag = True
    special_symbol = ""
    for i in string_container:
        if  not i.isalpha():
            flag = False
            special_symbol += " "+i
    if not flag:
        print("{} contain special symbol which is : {}".format(string_container,special_symbol))
    else:
        print("{} don't containe special symbol".format(string_container))

def regular_expression():
    string_container = "kas@hika$kha#tri"

    special_symbol = re.compile('[~!@#$%^&*<>?/\|{}:]')
    if special_symbol.search(string_container) != None:
        print("{} contain special symbol".format(string_container))
    else:
        print("{} don't containe special symbol".format(string_container))

   
native_method()
regular_expression()