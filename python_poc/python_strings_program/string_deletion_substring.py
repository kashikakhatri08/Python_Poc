def naive_method():
    string_container = "kaskashikahika"
    remove_string = "kashika"
    split_string =  string_container.split(remove_string)
    while len(string_container) != 0:
        split_string = string_container.split(remove_string)
        string_container = ""
        for i in split_string:
            string_container += i
    if string_container == "":
        print("substring can make string empty")
    else:
        print("substring can't make string empty")


def find_method():
    string_container = "kaskashikahika"
    remove_string = "kashika"

    while len(string_container) != 0:
        count = string_container.find(remove_string)
        if count == (-1):
            return False

        string_container = string_container[0:count] + string_container[count+len(remove_string):]

    return True



naive_method()

flag = find_method()
if flag:
    print("substring can make string empty")
else:
    print("substring can't make string empty")
