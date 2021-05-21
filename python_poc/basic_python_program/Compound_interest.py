
def user_input():
    principle = int(input("Enter the principle amount: "))
    rate = input("Enter the rate %: ")
    if type(rate) == int:
        rate = int(rate)
    else:
        rate = float(rate)
    time = input("enter the time: ")
    if type(time) == int:
        time = int(time)
    else:
        time = float(time)
    return principle, rate, time


def simple_interest(p, r, n):
    amount = p * pow((1 + r / 100), n)
    c_i = amount - p
    return c_i


def print_result(compound_interest_value):
    print("compound interest is : {}".format(compound_interest_value))


def main():
    p, r, n = user_input()
    compound_interest_value = simple_interest(p, r, n)
    print_result(compound_interest_value)


main()
print("-------------------")
