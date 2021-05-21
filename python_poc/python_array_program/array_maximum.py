def array_maximum():
    array_container = [7, 3, 8, 2, 9, 1]
    # logic1
    for i in range(1, len(array_container)):
        if array_container[i - 1] > array_container[i]:
            array_subsi = array_container[i - 1]
            array_container[i - 1] = array_container[i]
            array_container[i] = array_subsi
    print("array {} largest element is {} ".format(array_container, array_container[len(array_container) - 1]))

    # logic2
    array_max = array_container[0]
    for i in range(1, len(array_container)):
        if array_container[i] > array_max:
            array_max = array_container[i]
    print("array {} largest element is {} ".format(array_container, array_max))


array_maximum()
