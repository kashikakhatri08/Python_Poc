def user_input():
    print("this program will print even number in given array in a range which will give by user")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number :"))
    return start,end

def even_in_range(list_container,start,end):
    list_even = []
    if end >= len(list_container) or start >= len(list_container) or start < 0 or end <= -len(list_container):
        print("value given by user is out of range , given value  is not in between 0 to {}".format(len(list_container)-1))
        return []

    for i in range (start,end):
        if list_container[i] % 2 == 0:
            list_even.append(list_container[i])
    return list_even


def even_in_range_tech(start,end):
    even_list = range(start, end + 1)[start % 2::2]

    for num in even_list:
        print(num)


def main():
    list_container = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print("array:",list_container)
    start,end = user_input()
    list_even=even_in_range(list_container,start,end)
    if list_even == []:

        main()
    else:
        print(list_even)
    even_in_range_tech(start,end)

main()