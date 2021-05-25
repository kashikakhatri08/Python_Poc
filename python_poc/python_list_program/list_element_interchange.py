def interchange():
    list_container = [1,2,3,4,5]
    print(list_container)
    i =0
    temp= list_container[len(list_container)-1]
    list_container[len(list_container)-1] = list_container[i]
    list_container[i]=temp
    print(list_container)


interchange()