#Tuple In Python
'''
-Unchangable(Immutable)
-Tuple items are Ordered*
-Allow Duplicate Values
-use() to create a tuple
'''
#empty tuple
t1=()
t1=(1,2,3,4,5,'Akash',123.4)  #it can store different types of data
print(t1)
print(id(t1))
t1=1,2,3,4,5,6,6
print(t1)
print(id(t1))

thistuple=("apple","banana","cherry","apple",123,123.4)



#accesing the members of tuple
t1=1,2,3,4,5,6
print(t1[3])
print(t1[2])
print(t1[0])


#changing list into tuple
lst=[1,2,3,4,5]
t2=tuple(lst)
print(t2)


#Another Method to change the list into tuple
t3=tuple(lst)  #built in function in  python
print(t3)

#Function to Process Tuple
t1=(1,2,3,4,5,6,6)
print(len(t1))
print(min(t1))
print(max(t1))
print(t1.count(6))
print(t1.index(2))
print(sorted(t1 ,reverse=True))

"""
we cannot perform following operation in tuple
-append()
-extend()
-insert()
-clear()
because tuples are immutable.
"""


# 3.Set
"""
-{} for set
-set is a collection which is unordered
-unchangable(immutable)
-unindexed
-No duplicate members
[will automatically delete the duplicate elements from the set]
"""

setv={"apple","banana","cherry","apple",123,123}
print(setv)

print("__SET__")
t1={2,1,3,4,5,6,6}
print(t1)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1, reverse=True))
print(t1)
#print(t1.count(6))
#print(t1.index(6))

"""
we cannot perform these function in set
-append()
-extend()
-insert()
since set are immutable
"""
#Dictionary -> operations
"""
-it is a key value pair
-Dictionary is a collection which is orderes
-changeable
-No Duplicate Members
"""
#Dictionary items
car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=car.keys()
print(x)  #Before the change

car["color"]="white" #adding new value
car["brand"]="Ford123" #adding new value

x=car.keys()
print(x)       #After the change
y=car.values()
print(y)

#Duplicates are not allowed
thisdict={
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
        "year":2021,
        "year":2022,
        "year":2023,
        "year":1924,
}
print(thisdict)
#Removing keys
thisdict={
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
}
thisdict.popitem()
thisdict.pop("model")
print(thisdict)

#traversing Dictionaries
thisdict={
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
}
print()
print("dictionary: ")
for x in thisdict:
    print(x)
print()
print("keys: ")

for i in thisdict.keys():
    print(i,":",thisdict[i])
print()
print("values: ")
for i in thisdict.values():
    print(i)