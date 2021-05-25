def list_chunks():
    list_container = ['ka','sh','ik','a','kh','at','ri']
    n = 4
    list_chucnks = []
    res_list = []

    for i in range(0,len(list_container),n):
        for j in range(i,i+n):
            if j <len(list_container):
                list_chucnks.append(list_container[j])
        res_list.append(list_chucnks)
        list_chucnks = []

    print(res_list)

list_chunks()

def yield_method():
    list_container = ['ka', 'sh', 'ik', 'a', 'kh', 'at', 'ri']
    n = 4
    list_chucnks = []

    for i in range(0, len(list_container), n):
        yield list_container[i:i+n]

def list_comprehension_1():
    list_container = ['ka', 'sh', 'ik', 'a', 'kh', 'at', 'ri']
    n = 4
    final = [list_container[i * n:(i + 1) * n] for i in range((len(list_container) + n - 1) // n )]#// = floor //qtient
    print (final)

def list_comprehension_2():
    list_container = ['ka', 'sh', 'ik', 'a', 'kh', 'at', 'ri']
    n = 4
    list_chunks = [list_container[i:i+n] for i in range(len(list_container))]
    print(list_chunks)

list_chucnks = list(yield_method())
print(list_chucnks)
list_comprehension_1()
list_comprehension_2
