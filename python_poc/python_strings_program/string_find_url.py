import re


def regex():
    string_container = "My_Profile: https://github.com/kashikakhatri08/Python_Poc in https://github.com/"
    string_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    print_url = re.findall(string_regex,string_container)
    for i in print_url:
        print(i[0])

regex()