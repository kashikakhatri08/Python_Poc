from collections import Counter


def naive_frequency():
    string_container = "how how are you"
    count = 0
    string_sort = ""
    string_split = string_container.split(" ")
    print("in  ' {} ' string :".format(string_container))
    for i in range(len(string_split)):

        if string_sort.find(string_split[i]) == -1:
            for j in range(len(string_split)):

                if string_split[i] == string_split[j]:
                    count = count + 1
        if count > 0:
            string_sort = string_sort + string_split[i]
            print("{} frequency is {}".format(string_split[i], count))

        count = 0


def dict_frequency():
    string_container = "how how are you"
    string_count = {keys : string_container.count(keys) for keys in string_container.split()}
    print(string_count)

def counter_frequency():
    string_container = "how how are you"
    string_count =Counter(string_container.split())
    string_res = dict(string_count)
    print(string_res)

naive_frequency()
dict_frequency()
counter_frequency()