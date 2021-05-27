def native_method():
    string_container = "kashikaiskashika"
    replace_string = "kashika"
    string_container = string_container.replace("kashika","khatri")
    print(string_container)

def maketranse_translate():
    string_container = "kashikaforkashika"
    string_transe = str.maketrans("kashika","hellooo")#replace evry word with hello ex: k = o a =l
    string_container = string_container.translate(string_transe)
    print(string_container)

native_method()
maketranse_translate()
