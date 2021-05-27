def is_palindrome():
    string_container = "malayalam"
    reverse_string = ""

    for i in reversed(range(0, len(string_container))):
        reverse_string = reverse_string + string_container[i]
    if string_container == reverse_string:
        print("{} is palindrome".format(string_container))
    else:
        print("{} is not palindrome".format(string_container))

def slicing_method():
    string_container = "malayalam"
    reverse_string = string_container[::-1]
    if string_container == reverse_string:
        print("{} is palindrome".format(string_container))
    else:
        print("{} is not palindrome".format(string_container))


def using_join():
    string_container = "malayalam"
    reverse_string = "".join(reversed(string_container))
    """
    The join() method takes all items in an iterable and joins them into one string.
    A string must be specified as the separator.
    """
    if string_container == reverse_string:
        print("{} is palindrome".format(string_container))
    else:
        print("{} is not palindrome".format(string_container))


is_palindrome()
slicing_method()
using_join()
