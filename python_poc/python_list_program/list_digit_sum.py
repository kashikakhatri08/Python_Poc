def digit_sum():
    list_container = [12, 67, 98, 34]
    list_digit_sum = []

    for i in list_container:
        sum = 0
        for j in str(i):
            sum += int(j)
        list_digit_sum.append(sum)
    print(list_digit_sum)

def sum_method():
    list_container = [12, 67, 98, 34]
    list_digit_sum = list(map(lambda lists :sum(int(i)for i in str(lists) ),list_container))
    print(list_digit_sum)




sum_method()

#map
#https://realpython.com/python-map-function/
#lambda
#https://www.programiz.com/python-programming/anonymous-function


digit_sum()