#Accessing element from dictionory
import json

dict1={1:"kashika",2:"khatri",3:"Chinu"}
print(dict1)
print(dict1[1])
print(dict1.get(2))
json_data=json.dumps(dict1)
print("json",json_data)
#print(dict1[10])
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/DictionoryConcept7.py", line 6, in <module>
    print(dict1[10])
KeyError: 10
"""
print(dict1.get(20))
#None

print("#updating the elements")
dict1[2]="choti"
print(dict1)

print("#adding the elements")
dict1[4]="khatri"
print(dict1)

print("#remove an item")
dict2={1:1,2:2,3:3,4:4}
print(dict2)

print("remove one selected item")
print(dict2.pop(1))
print(dict2)

print("remove one arbitory item")
print(dict2.popitem())
print(dict2)

print("delete an item")
del dict2[2]
print(dict2)

#del dict2
#print(dict2)
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/DictionoryConcept7.py", line 41, in <module>
    print(dict2)
NameError: name 'dict2' is not defined

"""

print("#Creating a new dictionary using comprehension")
dict3={x:x*x for x in range(6)}
print(dict3)

print("#dictionary membership test")
dict4={1:1,3:9,5:25,7:49,9:81}
print(1 in dict4)
print(2 not in dict4)

print("#membership test for only key")
print(49 in dict4)

print("#iteration")
for i in dict4:
    print(dict4[i])

print("#using built-in function")
print(len(dict4))
print(sorted(dict4))