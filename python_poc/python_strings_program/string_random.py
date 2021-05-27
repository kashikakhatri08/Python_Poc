import random
import string


def random_method():
    string_container = "abc"
    i = ""
    count = 0
    while i != string_container:
        i ="".join(random.choice(string.ascii_lowercase + string.digits +
                     string.ascii_uppercase + ' ., !?;:')for k in range(len(string_container)))
        count = count+1
        print(i)
    print("target completed after {} iteration".format(count))

random_method()
