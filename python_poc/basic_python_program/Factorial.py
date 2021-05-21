def user_input():
    number = int(input("Enter the number: "))
    return number


def factorial(number):
    i = number
    while i > 1:
        number *= i-1
        i = i-1
    return number


def result_print(input_number, factorial_result):
    print("factorial of {} is : {}".format(input_number, factorial_result))


def main():
    input_number = user_input()
    factorial_result=factorial(input_number)
    result_print(input_number, factorial_result)


main()
