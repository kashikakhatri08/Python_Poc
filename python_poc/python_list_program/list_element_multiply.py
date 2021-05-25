import math
from functools import reduce

import numpy as numpy


def naive_method():
    list_container = [1,2,3,4,5]
    mul = 1
    for i in list_container:
        mul *= i
    print(mul)


def numpy_method():
    list_container = [1, 2, 3, 4, 5]
    mul_list = numpy.prod(list_container)
    print(mul_list)


def reduce_method():
    list_container = [1, 2, 3, 4, 5]
    mul_list = reduce(lambda x , y:x*y,list_container)
    print(mul_list)


def maths_prod_method():
    list_container = [1, 2, 3, 4, 5]
    mul_list = math.prod(list_container)
    print(mul_list)


naive_method()
numpy_method()
reduce_method()
maths_prod_method()
