def list_comprehension():
    list_container = [(),(3,4),(" "," "),(),(),(8," ")]
    tuple_free_list = [i for i in list_container if i]
    print(tuple_free_list)


def filter_method():
    list_container = [(), (3, 4), (" ", " "), (), (), (8, " ")]
    tuple_free_list = list(filter(None,list_container))
    print(tuple_free_list)

#filter
#https://www.programiz.com/python-programming/methods/built-in/filter#:~:text=Join-,Python%20filter(),to%20be%20true%20or%20not.


list_comprehension()
filter_method()