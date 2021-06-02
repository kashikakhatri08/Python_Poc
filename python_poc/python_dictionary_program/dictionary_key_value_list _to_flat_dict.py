def naive_method():
    dict_container = {"name":["kashika","jane","anne"],"age":[23,26,28]}
    dict_flat = {}
    for i in dict_container["name"]:
        for j in dict_container['age']:
            dict_flat[i] = j
    print(dict_flat)

def zip_method():
    dict_container = {"name": ["kashika", "jane", "anne"], "age": [23, 26, 28]}
    dict_flat = dict(zip(dict_container["name"],dict_container["age"]))
    print(dict_flat)


naive_method()
zip_method()