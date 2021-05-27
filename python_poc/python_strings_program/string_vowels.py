def naive_vowels():
    string_container = "haeElilou"
    count = 0
    string_vowels = ""
    vowels_tuple = ('a', 'e', 'i', 'o', 'u')

    for i in str(string_container):

        if i.casefold() not in string_vowels:
            if i in vowels_tuple:
                print("{} contains {}".format(string_container, i))
                string_vowels = string_vowels + i
                count += 1

    if count >= 5:
        print("{} contain all vowels".format(string_container))


def count_vowels():
    string_container = "haeElilou"
    string_lower = string_container.lower()
    string_vowels = [string_lower.count('a'),string_lower.count('e'),string_lower.count('i')
        ,string_lower.count('o'),string_lower.count('u')]
    if string_vowels.count(0) > 0:
        print("{} not contain all vowels".format(string_container))
    else:
        print("{} contain all vowels".format(string_container))


def intersection_vowels():
    string_container = "haeElilou"
    string_vowels = len(set(string_container.lower()).intersection('aeiou'))>= 5
    if string_vowels:
        print("{} contain all vowels".format(string_container))
    else:
        print("{} not contain all vowels".format(string_container))


naive_vowels()
count_vowels()
intersection_vowels()