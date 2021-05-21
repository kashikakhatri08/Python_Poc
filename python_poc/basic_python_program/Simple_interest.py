def user_input():
    principle = int(input("Enter the principle amount: "))
    rate = int(input("Enter the rate %: "))
    time = int(input("enter the time: "))
    return principle, rate, time


def simple_interest(p, r, t):
    s_i = (p * r * t) / 100
    return s_i


def print_result(simple_interest_value):
    print("simple interest is : {}".format(simple_interest_value))


def main():
    p, r, t = user_input()
    simple_interest_value = simple_interest(p, r, t)
    print_result(simple_interest_value)


main()
print("-------------------")
