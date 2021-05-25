def sorted_list():
    list_container_1 = ['a', 'd', 'g', 'b', 'e', 'h', 'c', 'f', 'i']
    list_container_2 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    zipped_list = zip(list_container_1, list_container_2)
    for _, x in sorted(zipped_list):
        print(x, _)


def dict_way():
    list_container_1 = ['a', 'd', 'g', 'b', 'e', 'h', 'c', 'f', 'i']
    list_container_2 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    # initializing blank dictionary
    f_1 = {}

    # initializing blank list
    final_list = []

    # Addition of two list in one dictionary
    f_1 = {list_container_1[i]: list_container_2[i] for i in range(len(list_container_2))}

    # sorting of dictionary based on value
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    # Element addition in the list
    for i in f_lst.keys():
        final_list.append(i)
    print(final_list)


# _ uses in python
# https://www.datacamp.com/community/tutorials/role-underscore-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034358&utm_targetid=aud-438999696719:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9050487&gclid=Cj0KCQjwwLKFBhDPARIsAPzPi-IUPregGMMneYEdIGwzzqR8CS3ka8npK-JJVN5RcrvUXISUti_He08aAoA0EALw_wcB#UIL

sorted_list()
dict_way()
