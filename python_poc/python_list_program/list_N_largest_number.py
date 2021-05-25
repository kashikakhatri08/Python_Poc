def naive_method():
    list_container = [5, 2, 7, 3, 9,10]
    number = 2
    #largest_num = list_container[0]


    list_final= []

    for i in range(0,number):
        largest_num = list_container[0]
        for j in range(len(list_container)):
            if largest_num < list_container[j]:
                largest_num=list_container[j]
        list_container.remove(largest_num)
        list_final.append(largest_num)
    print(list_final)


def sort_method():
    list_container = [5, 2, 7, 3, 9, 10]
    number = 3
    list_container.sort()
    final_list=[]
    final_list = list_container[-number:]
    print(final_list)


naive_method()
sort_method()
