print("#True false")
print(5 == 5)
print(5 > 5)

print("#NONE")
print(None == 0)
print(None == [])
print(None == False)
print(None == None)

def void_function():
    a=10
    b=10
    c=a+b
    #return(c)
func =void_function()
print(func)
#output: None(no return)

print("#and,or,not")
print(True or False)
print(True and False)
print(False and True)
print(False or True)
print(not False)

print("#as")
import math as myMath
print(myMath.cos(myMath.pi))

print("#assert")
#assert 5 > 5
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/KeywordsConcept3.py", line 32, in <module>
    assert 5 > 5
AssertionError
"""
assert 5>4
assert 5 == 5

print("#break")
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("#continue")
for i in range(1,11):
    if i == 5:
        continue
    print(i)

print("#class")
class ExampleClass:
    def function1(self):
        print("function1")
    def function2(self):
        print("function2")
obj = ExampleClass()
obj.function1()
obj.function2()

print("#def")
def function_name(parameter):
    pass
function_name(10)

print("#del")
a=10
print(a)
del a
#print(a)

print("#if..elif..else")
num = 2
if num == 1:
    print('one')
elif num == 2:
    print('two')
else:
    print('something else')

print("#try...raise...catch..finally")
try:
    x=9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution Successfully")

print("#for")
for i in range(1,10):
    print(i)

print("#from import")
import math
from math import cos
print(cos(1))

print("#global")
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar=5
def write2():
    globvar = 3
read1()
write1()
read1()
write2()
read1()

print("#in")
a = [1,2,3,4]
print(4 in a)

print("#is")
print(True is True)

print("#lambda")
a= lambda x:x*2
for i in range(1,6):
    print(a(i))

print("#nonlocal")
def outer_function():
    a=5
    def inner_function():
        nonlocal a
        a=10
        print("Inner Function",a)
    inner_function()
    print("oUTER Function",a)
outer_function()

print("#pass")
def function(args):
    pass

print("#return")
def func_return():
    a=10
    return a
print(func_return())

print("#while")
i=5
while(i>0):
    print(i)
    i -=i
print("#with")
with open('example.txt','w') as my_file:
    my_file.write("Hello World")

print("#yield")
def generator():
    for i in range(6):
        yield i*i
g=generator()
for i in g:
    print(i)


