def user_input():
    number = int(input("Enter the number: "))
    return number


def is_prime(i):
    if i == 2:
        print("{} is a prime number".format(i))
    elif i > 1:
        for j in range(2, i):
            if i % j == 0:
                print("{} is not a prime number".format(i))
                break
        else:
            print("{} is a prime number".format(i))
    else:
        print("{} is not a prime number".format(i))


def main():
    number = user_input()
    is_prime(number)


main()
