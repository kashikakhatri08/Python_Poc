def native_method():
    string_container = "kashikakhatri"
    n = 2
    n_part_1 =string_container[:n]
    rest_part_1 = string_container[n:]
    n_part_2 = string_container[len(string_container)-n:]
    rest_part_2 = string_container[:len(string_container)-n ]
    print(rest_part_2)

    #replace_string = "".join(string_container.replace(n_part,"")

    anti_clockwise__string = rest_part_1 +n_part_1
    clockwise_string = n_part_2+ rest_part_2
    print(anti_clockwise__string)
    print(clockwise_string)


native_method()