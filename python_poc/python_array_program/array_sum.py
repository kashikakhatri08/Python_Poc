def array_sum():
    array_container = [1, 2, 3, 4, 5]
    array_element_sum = 0
    for i in range(0, len(array_container)):
        array_element_sum += array_container[i]

    print("sum of array {} is :[{}]".format(array_container,array_element_sum))

array_sum()