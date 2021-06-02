from collections import Counter


def check_anagram():
    int_1 = 4
    int_2 = 8
    bin_1 = bin(int_1)
    bin_2 = bin(int_2)


    dict_container = {}
    dict_container[int_1] = list()
    dict_container[int_2] = list()

    for i in dict_container:
        if i == int_1:
            dict_container[i]= [i for i in bin_1]
        else:
            dict_container[i] = [i for i in bin_2]

    list_1 = dict_container.get(int_1)
    list_2 = dict_container.get(int_2)
    list_1 =sorted(list_1)
    list_2 = sorted(list_2)

    if len(list_1)>len(list_2):
        list_2.append("0")
    else:
        list_1.append("0")
    if list_1 == list_2:
        print("binary repersentation of {} , {} is anagram".format(int_1,int_2))
    else:
        print("binary repersentation of {} , {} is not anagram".format(int_1,int_2))


def counter_method():
    int_1 = 4
    int_2 = 8
    bin_1 = bin(int_1)[2:]
    bin_2 = bin(int_2)[2:]
    zeros = abs(len(bin_1) - len(bin_2))

    if len(bin_1) > len(bin_2):
        bin_2 = zeros * '0' + bin_2
        print(bin_2)
    else:
        bin_1 = zeros * '0' + bin_1
      
    dict_1 = Counter(bin_1)
    dict_2 = Counter(bin_2)
    if dict_1 == dict_2:
        print("binary repersentation of {} , {} is anagram".format(int_1, int_2))
    else:
        print("binary repersentation of {} , {} is not anagram".format(int_1, int_2))


check_anagram()
counter_method()