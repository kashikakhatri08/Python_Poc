import collections


def get_method():
    dict_container = {"a": 1, "b": 2}
    print(dict_container.get("a"))
    print(dict_container.get("c"))
    print(dict_container.get("c", "notfound"))


def setdefault_method():
    dict_container = {"a": 1, "b": 2}
    dict_container.setdefault("c", "not found")
    print(dict_container.get("a"))
    print(dict_container.get("c"))


def defaultDict_method():
    dict_container = collections.defaultdict(lambda: "not found")
    dict_container["a"] = 1
    dict_container["b"] = 2
    print(dict_container.get("a"))
    print(dict_container.get("c"))  # give none
    print(dict_container["c"])


get_method()
setdefault_method()
defaultDict_method()
