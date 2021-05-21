import math


def user_input():
    number = int(input("Enter number"))
    return number


def is_sqrt(number):
    square = int(math.sqrt(number))
    if square * square == number:
        return True
    else:
        return False


def is_fibonacci(number):
    if is_sqrt(5 * number * number + 4) or is_sqrt(5 * number * number - 4):
        print("{} is fibonacci".format(number))
    else:
        print("{} is not fibonacci".format(number))


def main():
    number = user_input()
    is_fibonacci(number)


main()
