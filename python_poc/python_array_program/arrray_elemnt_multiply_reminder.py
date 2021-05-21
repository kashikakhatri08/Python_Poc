# print the remainder after multiply all the number divide by n.
def user_input():
    global array_container

    array_length = int(input("Enter the array length : "))

    array_container = [None] * array_length
    for i in range(0, array_length):
        array_input = int(input("Enter the array element for array[{}] : ".format(i)))
        array_container[i] = array_input
    divider = int(input("Enter the number you want to divide the array elements multiplies: "))
    return divider


def multiply_then_divide(divider):
    mult_result = 1
    for i in range(0, len(array_container)):
        mult_result *= array_container[i]

    reminder = mult_result % divider
    print("after multiply element of array {}, result is: {}".format(array_container, mult_result))
    print("reminder of {} by {} is : {} ".format(mult_result, divider, reminder))


def main():
    divider = user_input()
    print("array :{}".format(array_container))
    multiply_then_divide(divider)


main()
