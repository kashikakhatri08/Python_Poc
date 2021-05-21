def user_input():
    character = input("Enter the char")
    return character


def char_into_ascii(character):
    ascii_value= ord(character)
    print("ascii value of char {} is : {}".format(character,
                                                  ascii_value))


def main():
    character = user_input()
    char_into_ascii(character)

main()