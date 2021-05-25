def duplicate_removal():
    list_container = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    list_duplicates = []

    for i in range(len(list_container)):
        for j in range(i + 1, len(list_container)):
            if list_container[i] not in list_duplicates:
                if list_container[i] == list_container[j]:
                    list_duplicates.append(list_container[i])

        for i in list_duplicates:
            for j in list_container:
                if i == j:
                    list_container.remove(j)

    print(list_duplicates)

    print(list_container)


duplicate_removal()
