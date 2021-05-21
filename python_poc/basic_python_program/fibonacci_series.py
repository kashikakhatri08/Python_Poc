def user_input():
    count = int(input("Enter the count: "))
    return count


def dynamic_fibonacci_series_fun(count):
    first=0
    second =1
    print("{} \n{}".format(first,second))

    for i in range(2,count+1):
        next_number = first+second
        first=second
        second=next_number
        print(next_number)

def recursive_fibonacci_series_fun(first,second,count):
    if count>0:
        next_number = first + second
        first = second
        second = next_number
        print(next_number)
        recursive_fibonacci_series_fun(first, second, count-1)


def main():
    count = user_input()
    dynamic_fibonacci_series_fun(count)
    print("----recursive----")
    first = 0
    second = 1
    print("{} \n{}".format(first, second))
    recursive_fibonacci_series_fun(first,second,count-1)


main()
