def user_input():
    number = int(input("Enter number"))
    position = int(input("Enter position"))
    return number, position


def is_fibonacci_multiple(number, position):
    first = 0
    second = 1
    i = 2
    while i != 0:
        next_number = first + second
        first = second
        second = next_number
        if second % number == 0:
            return position * i
        i += 1
    return


def main():
    number, position = user_input()
    print("fibonacci series {} th of {} multiple is : {} ".format(position, number,
                                                                  is_fibonacci_multiple(number, position)))
main()