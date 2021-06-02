from collections import defaultdict


def default_dict():
    dict_container = {"abc":[1,2,3],"bcd":[3,4],"cde":[1,4]}
    dict_new = defaultdict(list)
    for i,j in dict_container.items():
        for k in j:

            dict_new[k].append(i)
    print(dict(dict_new))

default_dict()
