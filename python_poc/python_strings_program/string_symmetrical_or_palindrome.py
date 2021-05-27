def is_symmetrical_or_palindrome():
    string_container = "amaama" #jojo
    string_half_1 = ""
    string_half_2 = ""
    for i in range(0,int(len(string_container)/2)):
        string_half_1 = string_half_1+string_container[i]
    for i in range(int(len(string_container)/2),int(len(string_container))):
        string_half_2 = string_half_2+string_container[i]
    if string_half_1 == string_half_2:
        print("{} is symmetrical".format(string_half_1))
    else:
        print("{} is  not symmetrical".format(string_half_1))
    reversed_second_half = string_half_2[::-1]

    if string_half_1 == reversed_second_half:
        print("{} is palindrome".format(string_half_1))
    else:
        print("{} is not palindrome".format(string_half_1))







is_symmetrical_or_palindrome()