"""

A cumulative sum is a sequence of partial sums of a given sequence. For example,
the cumulative sums of the sequence {a,b,c,...}, are a, a+b, a+b+c,
.... Cumulative sums are implemented as Accumulate[list].

"""

def cmulative_sum_1():
    list_container = [10,20,30,40,50]
    list_cmulative_sum = []
    list_sum = 0
    for i in range(len(list_container)):
        if i == 0:
            list_cmulative_sum.append(list_container[i])
        else:
            for j in range (0,i+1):
                list_sum += list_container[j]

            list_cmulative_sum.append(list_sum)
            list_sum = 0
    print(list_cmulative_sum)

def cmulative_sum_2():
    list_container = [10, 20, 30, 40, 50]
    list_cmulative_sum = []
    list_sum = 0
    for i in range(len(list_container)):
                list_sum += list_container[i]
                list_cmulative_sum.append(list_sum)
    print(list_cmulative_sum)


def cmlative_sum_3():
    list_container = [10, 20, 30, 40, 50]
    list_cmulative_sum = [sum(list_container[0:x:1] )for x in range(len(list_container)+1)]
    print(list_cmulative_sum[1:])
    for x in range(len(list_container)+1):
        #print(list_container[0:x])
        """
                output:-
                []
                [10]
                [10, 20]
                [10, 20, 30]
                [10, 20, 30, 40]
                [10, 20, 30, 40, 50]
        """
        print(sum(list_container[0:x]))
        '''
        output:-
        0
        10
        30
        60
        100
        150
        
        '''




cmulative_sum_1()
cmulative_sum_2()
cmlative_sum_3()





