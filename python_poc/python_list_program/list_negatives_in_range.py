def user_input():
    print("this program will print negative number in given array in a range which will give by user")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number :"))
    return start, end


def negative_in_range(list_container, start, end):
    list_positives = []
    if end >= len(list_container) or start >= len(list_container) or start < 0 or end <= -len(list_container):
       return []

    for i in range(start, end):
        if list_container[i] < 0:
            list_positives.append(list_container[i])
    return list_positives


def main():
    list_container = [1, -3, 9, 5, -6, 0]
    print("array:", list_container)
    start, end = user_input()
    list_positive = negative_in_range(list_container, start, end)
    if not list_positive:
        print("value given by user is out of range , given value is  not in between 0 to {} or in incressing order".format(
            len(list_container) - 1))
        main()
    else:
        print(list_positive)


main()
