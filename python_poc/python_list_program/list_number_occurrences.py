from collections import Counter


def naive_method():
    list_container = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
    count = 0
    find_count = 6
    for i in list_container:
        if i == find_count:
            count = count + 1
    print(count)


def count_method():
    list_container = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
    find_count = 6
    count = list_container.count(find_count)
    print(count)


def counter_method():
    list_container = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
    find_count = 6
    count_dict = Counter(list_container)
    print(count_dict[find_count])


def count_every_element_occurrence():
    list_container = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]
    count = 0
    for i in list_container:
        for j in list_container:
            if i == j:
                count = count + 1
        print("{} elemt is persent in {} ,{} times".format(i,list_container,count))
        count = 0


naive_method()
count_method()
counter_method()
count_every_element_occurrence()
