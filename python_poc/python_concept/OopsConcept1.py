class Example1:
    #constructor__init__
    #self:denoting interfrence of object(this)
    #known as "this reference"
    def __init__(self,name):
        self.name=name

    def fullname(self):
        print("{0}".format(self.name))#{0}whil take 1st argument


name_1=Example1("kashika")
#attribute define by object
name_1.age=23
name_1.fullname()
print(name_1.age)

name_2=Example1("khatri")

#name_2.myName
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/OopsConcept1.py", line 18, in <module>
    name_2.myName
AttributeError: 'Example1' object has no attribute 'myName'
"""

#deleting new object and attribute
name_2.height=4.9
print(name_2)
del name_2.height
del name_2
#print(name_2)
"""
Traceback (most recent call last):
  File "/home/kashika/python_poc/OopsConcept1.py", line 33, in <module>
    print(name_2)
NameError: name 'name_2' is not defined

"""