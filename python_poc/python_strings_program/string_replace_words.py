import re


def native_method():
    string_container = "hello my name is kashika "
    replace_list = ["my","name","is"]
    res_str = " "
    split_string = string_container.split()
    for i in split_string:
        if i in replace_list:
            res_str += " " +i.replace(i,"khatri")
        else:
            res_str += " "+i
    print(res_str)

def join_split():
    string_container = "hello my name is kashika "
    replace_list = ["my", "name", "is"]
    split_string = string_container.split()
    out_str = "khatri"
    res_str = " ".join(out_str if i in replace_list else i for i in split_string)
    print(res_str)

def regex_join():
    string_container = "hello my name is kashika "
    replace_list = ["my", "name", "is"]

    out_str = "khatri"
    res_str = re.sub("|".join(sorted(replace_list, key=len, reverse=True)), out_str, string_container)
    print(res_str)



native_method()
join_split()
regex_join()