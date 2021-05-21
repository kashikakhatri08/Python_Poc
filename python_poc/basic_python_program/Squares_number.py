def user_input():
    number = int(input("Enter number"))
    return number


def squares_number(number):
    sum = 0
    for i in range(0, number + 1):

        sum += pow(i, 2)
      
    print("square of number till position {} is: {}".format(number, sum))


def main():
    number = user_input()
    squares_number(number)


main()
