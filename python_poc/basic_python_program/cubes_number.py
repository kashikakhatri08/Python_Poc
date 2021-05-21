def user_input():
    number = int(input("Enter number"))
    return number


def cubes_number(number):
    cubes_sum = 0
    for i in range(0, number + 1):
        cubes_sum += pow(i, 3)

    print("square of number till position {} is: {}".format(number,  cubes_sum))


def main():
    number = user_input()
    cubes_number(number)


main()
