def user_input():
    pos1 = int(input("Enter position1 number: "))
    pos2 = int(input("Enter position2 number: "))
    return pos1,pos2


def swap_position_aprroach1(list_container,pos1,pos2):

    temp= list_container[pos2]
    list_container[pos2] = list_container[pos1]
    list_container[pos1]=temp
    print(list_container)


def swap_position_aprroach2(list_container, pos1, pos2):
    list_container[pos1],list_container[pos2]=list_container[pos2],list_container[pos1]
    print(list_container)


def swap_position_aprroach3(list_container, pos1, pos2):
    temp1 = list_container.pop(pos1)
    temp2 = list_container.pop(pos2-1)
    list_container.insert(pos1,temp2)
    list_container.insert(pos2,temp1)
    print(list_container)


def swap_position_aprroach4(list_container, pos1, pos2):
    print(list_container)
    tup = list_container[pos1],list_container[pos2]
    print(tup)
    list_container[pos2],list_container[pos1] = tup
    print(list_container)


def main():
    list_container = [1, 2, 3, 4, 5]
    print("array is :",list_container)
    print("Enter the postion number 0 to  {}".format(len(list_container)-1))
    pos1,pos2 = user_input()
    swap_position_aprroach1(list_container,pos1,pos2)
    swap_position_aprroach2(list_container, pos1, pos2)
    swap_position_aprroach3(list_container, pos1, pos2)
    print(list_container)
    swap_position_aprroach4(list_container, pos1, pos2)
    #function change list value permantally

main()