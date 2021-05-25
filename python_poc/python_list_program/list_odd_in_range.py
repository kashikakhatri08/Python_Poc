def user_input():
    print("this program will print even number in given array in a range which will give by user")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number :"))
    return start,end

def odd_in_range(list_container,start,end):
    list_odd= []
    if end >= len(list_container) or start >= len(list_container) or start < 0 or end <= -len(list_container):
        print("value given by user is out of range plz give value  not in between 0 to {}".format(len(list_container)-1))
        return []

    for i in range (start,end):
        if list_container[i] % 2 != 0:
            list_odd.append(list_container[i])
    return list_odd





def main():

    list_container = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print("array:",list_container)
    start,end = user_input()
    list_odd=odd_in_range(list_container,start,end)
    if list_odd == []:

        main()
    else:
        print(list_odd)



main()