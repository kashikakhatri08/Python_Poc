def user_input():
    global array_container

    array_length = int(input("Enter the array length : "))

    array_container = [None] * array_length
    for i in range(0, array_length):
        array_input = int(input("Enter the array element for array[{}] : ".format(i)))
        array_container[i] = array_input
    shift_by_position = int(input("Enter the number you want to shift the array: "))
    return shift_by_position


def array_rotation_by_one():
    array_rotate_container = [None] * len(array_container)
    j = 0
    for i in reversed(range(len(array_container))):
        array_rotate_container[j] = array_container[i]
        j = j + 1

    print(array_rotate_container)


def array_rotation_by_any(shift_by_position):
    array_rotate_container = [None] * len(array_container)
    j = len(array_rotate_container) - shift_by_position
    for i in range(0, len(array_container)):
        if j < len(array_rotate_container):
            array_rotate_container[j] = array_container[i]
            j = j + 1
    j = 0
    for i in range(shift_by_position, len(array_container)):
        array_rotate_container[j] = array_container[i]
        j = j + 1
    print(array_rotate_container)


def main():
    shift_by_position = user_input()
    print("array is : {}".format(array_container))
    print("given array element in revers: ")
    array_rotation_by_one()
    print("given array shifted by {} position is :".format(shift_by_position))
    array_rotation_by_any(shift_by_position)


main()
