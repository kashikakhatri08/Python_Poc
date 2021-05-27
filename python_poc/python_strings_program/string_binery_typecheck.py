def check():
    string_container = "010ka10101"
    set_string = set(string_container)
    set_binery = {0,1}
    flag = True
    if set_string == set_binery or set_string == {0} or set_binery == {1}:
        pass
    else:
        flag = False
    if flag:
        print("binery")
    else:
        print("not binery")

def naive_method():
    string_container = "01010ka101"
    flag = True
    for i in string_container:
        if i == "0" or i == "1":
            pass
        else:
            flag = False
    if flag:
        print("binery")
    else:
        print("not binery")


if __name__ == '__main__':
    check()
    naive_method()