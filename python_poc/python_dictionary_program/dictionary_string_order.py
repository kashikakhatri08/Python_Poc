from collections import OrderedDict


def naive_method():
    string_container = "abcde de"
    #example "engineers rock" pattern: egr
    pattern = "de"
    flag = True
    for i,j in enumerate(string_container):
        if j == "d":
            if "e" in string_container[:i]:
                flag = False


        if j == "e":
            if "d" in string_container[i:len(string_container)]:
                flag =False


    if flag:
        print("True")
    else:
        print("false")

naive_method()



def orderdict_method():
    string_container = "kanko on"
    pattern = "ko"
    order_string_dict = OrderedDict.fromkeys(string_container)
    num = 0
    flag = False
    for i,j in order_string_dict.items():
        if i == pattern[num]:
            num = num +1
        if num == (len(pattern)):
            flag = True
            break

    if flag:
        print("True")
    else:
        print("false")



orderdict_method()