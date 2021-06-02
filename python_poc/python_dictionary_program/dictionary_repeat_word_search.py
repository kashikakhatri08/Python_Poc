from collections import Counter


def naive_method():
    string_container = "Python is great and Java is also great"
    string_container = string_container.split(" ")
    dict = Counter(string_container)
    result = " ".join(dict.keys())
    print(result)

def alternative_method():
    string_container = "Python is great and Java is also great"
    list_container = string_container.split(" ")
    list_result = []
    for i in list_container:
        if(string_container.count(i)>1 and (i not in list_result) or string_container.count(i)==1):
            list_result.append(i)
    result = " ".join(list_result)
    print(result)
naive_method()
alternative_method()
