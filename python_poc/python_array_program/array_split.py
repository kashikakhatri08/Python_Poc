def user_input():
    global array_container

    array_length = int(input("Enter the array length : "))

    array_container = [None] * array_length
    for i in range(0, array_length):
        array_input = int(input("Enter the array element for array[{}] : ".format(i)))
        array_container[i] = array_input
    split_by_position = int(input("Enter the number you want to split the array: "))
    return split_by_position


def splitarray():
    array_split_container = [None] * len(array_container)
    split = 0
    if len(array_split_container) % 2 == 0:

        split = int(len(array_container) / 2)
    else:
        split = int(len(array_container) / 2) + 1

    print(split)
    j = len(array_container) - split

    for i in range(0, split):
        array_split_container[j] = array_container[i]
        j = j + 1
    j = 0
    if j < split:
        for i in range(split, len(array_container)):
            array_split_container[j] = array_container[i]
            j = j + 1
        print(array_split_container)


def splitbyposition(split_by_position):
    array_split_container = [None] * len(array_container)

    j = len(array_container) - split_by_position

    for i in range(0, split_by_position):
        array_split_container[j] = array_container[i]
        j = j + 1
    j = 0
    if j < split_by_position:
        for i in range(split_by_position, len(array_container)):
            array_split_container[j] = array_container[i]
            j = j + 1
        print(array_split_container)


def main():
    global array_container
    split_by_position = user_input()
    array_container = [1, 2, 3, 4, 5, 6, 7]
    print("array : ")
    print(array_container)
    print("slit array from middle and add first part to the end part")
    splitarray()
    print("split array at {} position".format(split_by_position))
    splitbyposition(split_by_position)


main()
