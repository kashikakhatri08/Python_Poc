def naive_method():
    dict_container_1 = {1: 10, 2: 20, 3: 30, 4: 40}
    dict_container_2 = {5: 50, 6: 60, 7: 70, 8: 80}
    for i in dict_container_2:
        dict_container_1[i] = dict_container_2.get(i)

    print(dict_container_1)


def update_method():
    dict_container_1 = {1: 10, 2: 20, 3: 30, 4: 40}
    dict_container_2 = {5: 50, 6: 60, 7: 70, 8: 80}
    merged_dict = dict_container_1.update(dict_container_2)
    print(merged_dict)
    print(dict_container_1)


def double_asterisk_method():
    dict_container_1 = {1: 10, 2: 20, 3: 30, 4: 40}
    dict_container_2 = {5: 50, 6: 60, 7: 70, 8: 80}
    merged_dict = {**dict_container_1, **dict_container_2}
    print(merged_dict)




naive_method()
update_method()
double_asterisk_method()
