def naive_length_find():
    string_container = "kashika"
    count = 0
    for i in str(string_container):
        count = count + 1

    print("string '{}' length is : {}".format(string_container, count))


def len_method():
    string_container = "kashika"
    count = len(string_container)
    print("string '{}' length is : {}".format(string_container, count))


def while_slicing_count():
    string_container = "kashika"
    count = 0

    while string_container[count:]:
        count = count + 1

    print("string '{}' length is : {}".format(string_container, count))


def join_method():
    string_container = "kashika"
    string_add = "kh"
    count = (string_add.join(string_container)).count(string_add) + 1
    print("string '{}' length is : {}".format(string_container, count))


naive_length_find()
len_method()
while_slicing_count()
join_method()

