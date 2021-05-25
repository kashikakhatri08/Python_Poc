def user_input():
    element = int(input("Enter element you want to search: "))
    return element

def naive_method(element):
    list_container = [1,2,3,4,5]

    for i in range(len(list_container)):
        if element == list_container[i]:
            return True



def in_method(element):
    list_container = [1, 2, 3, 4, 5]

    if element in list_container:
        return True


def main():
    list_container = [1, 2, 3, 4, 5]
    print(list_container)
    element = user_input()
    naive_reply = naive_method(element)

    if naive_reply:
        print("{} is persent in {}".format(element, list_container))
    else:
        print("{} is not persent in {}".format(element, list_container))

    in_reply =  in_method(element)

    if in_reply:
        print("{} is persent in {}".format(element, list_container))
    else:
        print("{} is not persent in {}".format(element, list_container))


main()