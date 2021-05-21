def user_input():
    number = int(input("Enter the number: "))
    return number


def armstrong_number_check(number):
    count = 0
    reminder = []
    result = 0
    while number != 0:
        quotient = int(number / 10)
        reminder.append(number % 10)
        number = quotient
        count = count + 1
    while len(reminder) > 0:
        result += pow(reminder.pop(), count)

    return result


def main():
    number = user_input()
    result = armstrong_number_check(number)
    if number == result:
        print("{} is armstrong number".format(number))
    else:
        print("{} is not a armstrong number".format(number))


main()
