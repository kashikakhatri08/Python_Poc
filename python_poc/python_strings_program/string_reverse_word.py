def reverse_string():
    string_container = "kashika khatri"
    string_reverse = ""
    string_words = string_container.split(" ")
    for i in reversed(range(0, len(string_words))):
        string_reverse = string_reverse+" "+string_words[i]
    print(string_reverse)


reverse_string()