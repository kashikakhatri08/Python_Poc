from collections import OrderedDict


def non_repeating():
    string_container = "kashikakhatri"
    k = 3
    dict = {}
    for i in string_container:
        if i in dict.keys():
            dict[i] = dict.get(i)+1
        else:
            dict[i] = 0
    order_list_1 = OrderedDict(dict)
    order_list = [i for i,j in order_list_1.items() if dict.get(i) == 0 ]
    if k <= len(order_list):
        for i in range(0,len(order_list)):

            if i == k-1:
                print("3rd non-repeating element of {}  string is : {}".format(string_container,order_list[i]))
    else:
        print("number given for finding non-repeating element is out of bound")
non_repeating()