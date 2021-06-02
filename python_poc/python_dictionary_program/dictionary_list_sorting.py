from operator import itemgetter


def naive_method():
    dict_container = [{"name": "kashika", "age": 23}, {"name": "jhon", "age": 28}, {"name": "anne", "age": 26}]
    # sorted by both name and age but priority will be name
    sorted_list_1 = sorted(dict_container, key=lambda i: (i["name"], i["age"]))
    # sorted by name
    sorted_list_2 = sorted(dict_container, key=lambda i: (i["name"]))
    # sorted by age
    sorted_list_3 = sorted(dict_container, key=lambda i: (i["age"]))
    # sorted by both name and age but priority will be age
    sorted_list_4 = sorted(dict_container, key=lambda i: (i["age"], i["name"]))
    # sorted by age in descending
    sorted_list_5 = sorted(dict_container, key=lambda i: (i["age"]), reverse=True)
    print(sorted_list_1)
    print(sorted_list_2)
    print(sorted_list_3)
    print(sorted_list_4)
    print(sorted_list_5)

def itemgetter_method():
    dict_container = [{"name": "kashika", "age": 23}, {"name": "jhon", "age": 28}, {"name": "anne", "age": 26}]
    sorted_list_1 = sorted(dict_container,key = itemgetter("name"))
    sorted_list_2 = sorted(dict_container,key = itemgetter("age"))

    sorted_list_3 = sorted(dict_container,key = itemgetter("name","age"))

    sorted_list_4 = sorted(dict_container,key = itemgetter("age","name"))
    sorted_list_5 = sorted(dict_container,key = itemgetter("name"),reverse=True)
    print(sorted_list_1)
    print(sorted_list_2)
    print(sorted_list_3)
    print(sorted_list_4)
    print(sorted_list_5)




naive_method()
itemgetter_method()

