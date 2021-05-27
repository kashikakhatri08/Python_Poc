def naive_method():
    string_container_1 = "hello how are you?"
    string_container_2 = "hi who are you?"
    split_1 = string_container_1.split()
    split_2 = string_container_2.split()
    string_list = []
    for i in range(len(split_1)):
        if split_1[i] not in split_2:
            string_list.append(split_1[i])
    for j in range(len(split_2)):
        if split_2[j] not in split_1:
            string_list.append(split_2[j])

    print(string_list)

def symmetric_diffrence():
    string_container_1 = "hello how are you?"
    string_container_2 = "hi who are you?"
    split_1 = string_container_1.split()
    split_2 = string_container_2.split()
    diff = set(split_1).symmetric_difference(split_2)
    print(diff)

def dictionory_method():
    string_container_1 = "hello how are you?"
    string_container_2 = "hi who are you?"
    dict_string = {}
    split_1 = string_container_1.split()
    split_2 = string_container_2.split()
    for i in range(len(split_1)):
        dict_string[split_1[i]] = dict_string.get(split_1[i],0)+1
    for i in range(len(split_2)):
        dict_string[split_2[i]] = dict_string.get(split_2[i], 0)+1
    print_string = [i for i in dict_string if dict_string[i] == 1]
    print(print_string)



naive_method()
symmetric_diffrence()
dictionory_method()