#defining and declaring an array
arr=[10,20,30,40,50]
print(arr)

#Accessing Array elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) #last element
print(arr[-2]) #second last element

brands=['Coke','Apple','Google','Microsoft','Toyota']
 #Finding the length of the array
print(brands)
num_brands=len(brands)
print(num_brands)

#Adding an element to an array using append()
brands.append('Intel')
print(brands)

#Removing elements from an array
colors=["violet","indigo","blue","green","yellow","orange","red"]
print(colors)
del colors[4]
print(colors)
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)

#modifying elements of an array using indexing
fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits)
fruits[1]="Pineapple"
print(fruits)
fruits[-1]="Guavae"
print(fruits)

#Concatenating two arrays using the + operator
concat=[1,2,3]
print(concat)
concat=concat + [4,5,6]
print(concat)

#Repeating element in an array
Repeat =["a"]
Repeat =Repeat * 5
print(Repeat)

#Slicing an array
fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits[1:4])
print(fruits[ :3])
print(fruits[-4: ])
print(fruits[-3:-1])

#Declaring and defining multidimensional array
multd=([1,2],[3,4],[5,6],[7,8])
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])






