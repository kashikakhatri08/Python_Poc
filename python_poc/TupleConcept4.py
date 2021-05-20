#tuple
print("#creating a empty tuple")
tuple1=()
print(tuple1)

print("#creating a tuple with integer element")
tuple2=(1,2,3,4)
print(tuple2)

print("#creating a tuple with mixed element")
tuple3=(1,2.03,"Number")
print(tuple3)

print("#nested tuple")
tuple4=(1,(1,2,3),[1,2,3])
print(tuple4)

print("#tuple without parathences")
#tuple packing
tuple5= 101,"hello",3.14,"Hello world"
print(tuple5)

print("#tuple unpackingpring")
var1,var2,var3,var4=tuple5
print(var1)
print(var2)
print(var3)
print(var4)
print(type(tuple5))

print("#accessing tuple elements")
tuple6=('h','e','l','l','o')
print(tuple6)
print(tuple6[0])
print(tuple6[2])
print(tuple6[4])

print("#nested tuple elements accessing")
tuple7=("hello",[1,2,3],(4,5,6))
print(tuple7)
print(tuple7[0][3])
print(tuple7[1][2])
print(tuple7[2][2])

print("#slicing tuple elements")
tuple8=('h','e','l','l','o')
print(tuple8[:3])
print(tuple8[:-3])
print(tuple8[3:])
print(tuple8[:])

print("#tuples are immutable")
tuple9=('h','e','l','l','o')
print(tuple9)
#tuple9[2]='L'
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/TupleConcept4.py", line 55, in <module>
    tuple9[2]='L'
TypeError: 'tuple' object does not support item assignment
"""

print("#tuples can exchange")
tuple9=('w','o','r','l','d')
print(tuple9)

print("#concatation of tuples")
tuple10=('h','e','l','l','o')
tuple11=('w','o','r','l','d')
print(tuple10)
print(tuple11)
print(tuple10+tuple11)
print(("again",)*4)

print("#deleation")
tuple12=(1,2,3,4,5)
#del tuple12[2]
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/TupleConcept4.py", line 77, in <module>
    del tuple12[2]
TypeError: 'tuple' object doesn't support item deletion
"""
del tuple12

print("#tuple method")
tuple13 = ('a','d','c','c','k','a')
print(tuple13)
print(tuple13.count('c'))
print(tuple13.index('a'))

print("#tuple operation")
tuple14=('h','e','l','l','o')
print('e' in tuple14)
print('a' not in tuple14)

print("#iteration")
tuple15=('h','e','l','l','o',' ','w','o','r','l','d')
for letters in tuple15:
    print("letters ->",letters)

print("#built-in function")
tuple16=(23,78,11,54,93,1)
print(max(tuple16))
print(min(tuple16))
print(sorted(tuple16))
print(len(tuple16))
