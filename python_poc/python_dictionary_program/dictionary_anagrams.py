def anagrams_print():

    list_container = ['cat', 'dog', 'tac', 'god', 'act']
    dict_container = {}
    output = " "
    for i in list_container:
        key = "".join(sorted(i))

        if key in dict_container.keys():
            dict_container[key].append(i)
        else:
            dict_container[key] =[]
            dict_container[key].append(i)

    for key,value in dict_container.items():
        output = output +" ".join(value)+' '

    print(output)



anagrams_print()