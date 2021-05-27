from collections import OrderedDict


# fromkeys() creates a new dictionary with keys from seq and values set to value and returns list of keys,
# fromkeys(seq[, value]) is the syntax for fromkeys() method.

# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

def naive_method():
    string_container = "kashika"
    string_unique = ""

    for i in string_container:
        for j in string_container:
            if i not in string_unique:
                if i == j:
                    string_unique += i

    print(string_unique)


def set_method():
    string_container = "kashika"
    string_unique_unordered = "".join(set(string_container))
    print(string_unique_unordered)
    string_unique_ordered = "".join(OrderedDict.fromkeys(string_container))
    print(string_unique_unordered)


naive_method()
set_method()
