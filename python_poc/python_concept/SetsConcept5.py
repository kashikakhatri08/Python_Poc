print("#creation of sets")
print("#sets of integer value")
set1={11,22,33,44,55}
print(set1)

print("#sets of mixed integer")
set2={1,"hello",2.3,(22,33)}
print(set2)

print("#duplicate values are not allowed")
set3={11,22,33,44,55,44}
print(set3)

print("#sets can't have mutable elements")
#set4={1,2,[3,4]}
#print(set4)
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/SetsConcept5.py", line 15, in <module>
    set4={1,2,[3,4]}
TypeError: unhashable type: 'list'
"""
print("#can make sets from list")
listToSets=set([1,2,3])
print(listToSets)
print(type(listToSets))

print("#can make list from sets")
SetsToList=list({1,2,3})
print(SetsToList)
print(type(SetsToList))

print("#sets operation")
#print("#sets not supporinting indexing")
set5={11,22,33,44,55}
#set5[2]
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/SetsConcept5.py", line 35, in <module>
    set5[2]
TypeError: 'set' object is not subscriptable
"""
print("add one element")
set5.add(66)
print(set5)

print("#add multiple elements")
set5.update([77,88,99])
print(set5)

print("#add sets and list")
set5.update([100,110,120],(130,140,150))
print(set5)

print("#remove and discard")
set6={11,22,33,44,55}
print(set6)
print("#discard an element which is not persent,no error")
print(set6.discard(66))
print(set6)
#print("#remove an element which is not persent,error")
#print(set6.remove(66))
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/SetsConcept5.py", line 60, in <module>
    print(set6.remove(66))
KeyError: 66
"""

print("#discard an element")
print(set6.discard(55))
print(set6)

print("#remove an element")
print(set6.remove(44))
print(set6)

print("#using pop()")
set7={11,22,33,44,55}
print(set7)

set7.pop()
print(set7)

print("#clear a set")
set7.clear()
print(set7)

print("#set operation")
set8={1,2,3}
set9={4,5,6}
print(set8)
print(set9)

print("Union- use | for union")
print(set8 | set9)
print(set9 | set8)
print(set8.union(set9))
print(set8.union(set9))

set10={1,2,3,4,5}
set11={4,5,6,7,8}
print(set10)
print(set11)

print("Intersection- use & for Intersection")
print(set10 & set11)
print(set11 &  set10)
print(set10.intersection(set11))
print(set11.intersection(set10))

print("difference- use - for difference")
print(set10 - set11)
print(set11 -  set10)
print(set10.difference(set11))
print(set11.difference(set10))

print("symmetric_difference- use ^ for symmetric_difference")
print(set10 ^ set11)
print(set11 ^  set10)
print(set10.symmetric_difference(set11))
print(set11.symmetric_difference(set10))

print("#set membership")
set12={1,2,3,4,5}
print(2 in set12)
print(2 not in set12)
print(6 in set12)
print(6 not in set12)

print("#iteration")
for letters in set("Welcome"):
    print("letters ->",letters)

print("Buil-in function")
set13={1,2,3,4,5}
print(set13)
print("len()",len(set13))
print("min()",min(set13))
print("max()",max(set13))
print("sorted",sorted(set13))

"""
python frozenset
frozenset is a new class that has characteristics
of a set,but its elemets cannot be changed onece assigned
while tuples are immutable lists ,frozensets are immutable sets
initialize A and B
"""
set14=frozenset([1,2,3,4])
set15=frozenset([3,4,5,6])
print(set14)
print(set15)
print(set14.difference(set15))
print(set14.union(set15))
print(set14.symmetric_difference(set15))
print(set14.intersection(set15))
#set14.add(7)
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/SetsConcept5.py", line 158, in <module>
    set14.add(7)
AttributeError: 'frozenset' object has no attribute 'add'
"""
