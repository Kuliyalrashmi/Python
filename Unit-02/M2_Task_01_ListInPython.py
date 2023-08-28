#List
'''
Data Structures :Lists
-Basic list operations 
    -Creating a list
    -inserting
    -Replacing
    -Removing an element
    -searching
    -Sorting a list
-Methods of list objects
-Nested list
-Using Lists as Stacks And Queues
-How efficient lists are when as stacks and queues
'''
# 1.What is list in python?
"""
-List is a Python's inbuilt data structure
-List can store different type of elements whereas array can stores only sigle type of elements [int arr[3]={1,2,3}]
-[], Square brackets are used to create a list++
"""
#1.1 empty list example
listSample=[]
print(listSample) #[]

#2.Create a list!
participants=['john','Rakesh','Amit','Suresh',123,123.4,'A']
print(participants)
print(participants[1]) #Rakesh
print(participants[4]) #123
print(participants[0]) #john
print(participants[-1])#A
print(participants[-2])#123.4

#3 Updating a list element
participants[3]='Maria'
print(participants) #['john','Rakesh','Amit','Maria',123,123.4,'A']

#4.Delete an element from the list

del participants[2]
print(participants) #['john','Rakesh','Maria',123,123.4,'A']

#delete a set of elements from a list
del participants[1:3]
print(participants) #['john',123,123.4,'A']


#5.Add new elements into a list
participants.append("rashmi")
participants.append("abc")
participants.append("def")
participants.append("987")
print(participants) #['john', 123, 123.4, 'A', 'rashmi', 'abc', 'def', '987']


#6. Replace Values in a List using indexing
l=['Rashmi','uma','chahak','kajal']
l[0]='abc'
print(l) #['abc', 'uma', 'chahak', 'kajal']


#7.List Slicing
"""
list[index]
list[start,stop]
list[start,stop,step]
stop element would be excluded from the end result
"""
l=['Rashmi','uma','chahak','kajal','rashmi']
print(l)
print(l[1:3])
print(l[:2])
print(l[4:])
print(l[-2:])
print(l[-2::-1])

#8. Find index of an element of the list
Maria_index=l.index("rashmi")
print(Maria_index)
#Value Error:"Maria not in list"
# index=participants.index("Maria123")
# print(index)


#9. Search an element in a list
x=[1,2,3,4,5]
print(2 in x)
print(7 not in x)

participants=['suresh','john','maria','Amit','Sumit','cat']
x=[1,2,3,4,5]
b=7
if b in x:
    a=x.index(b)
    print(a)
else:
    print("Element not found in the list")


#10.  Sort a list
participants.sort()
print(participants)

#11 . sort in reverse order
participants.sort(reverse=True)
#the change will take place in the original string only,as 
#list is mutable in python 
print(participants)

Numbers=[2,3,4,5,1]
Numbers.sort()
print(Numbers)
Numbers.sort(reverse=True)
print(Numbers)

#12.Creating a list using range function [list comprehension]
lst=range(1,9,2)
for i in lst:
    print(i)


#13. Concat two lists
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)  # It will create a list of Combined elements

#14. Nested list as Matrices[Nested List]
participants=['suresh','john','maria','Amit','Sumit','cat',123]
Newcomers=['joshua','Brittany']
print("__Bigger_List__")
Bigger_List=[participants,Newcomers]
print(Bigger_List)
print(Bigger_List[0])
print(Bigger_List[1])
print(Bigger_List[0][4])
print(Bigger_List[0][5])
print(Bigger_List[0][2])
print(Bigger_List[1][1])
# print(Bigger_List[4])   #Index range out of bound

# 15.Find max and min from list
Numbers=[1,2,3,4,5]
print(max(Numbers))
print(min(Numbers))


#16. Extra Methods of List Objects
n=[1,2,3,4,5,6]
print(len(n))
n.append(7)
n.append(7)
print(n)
print(n.count(7))

#elemnets based
n.remove(7)
print(n)

#index based
n.pop()
n.pop(0)
print(n)


#reverse list
n.reverse()
print(n)


n.clear()  # Delete all elements of the list ad would leave only empty list at the end
print(n)


#17. list Comprehension
''' 
List comprehension represents creation of new list from an iterable object like range ,set,tuple and so on
'''
s=[]
for i in range(1,9):
    s.append(i)


print(s)

lst=range(1,9,2)
for i in lst:
    print(i)


#yet to explore :set ,tuple,dictionary->list

#18. using list as a stack
#LIFO ORDER
stack=['Amar','Akbar','Anthony']
stack.append('ram')
stack.append('Iqbal')
print(stack)


#Removes the last item
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


# 19.Using List As Queues
#FIFO Order
queue=[]
queue.append('a')
queue.append('a')
queue.append('a')
queue.append('a')
queue.append('a')
print(queue)

#renmoving ellement from queue
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)


#How efficient lists are when used as a stack or queue
#As Stack
"""
-The Biggest issue is that it can run into speed issues as it grows
-The items in the list are stored next to each other in memory,
-If the stack grows bigger than the block of memory that currently holds,then python needs to do some memory allocation. this can lead to some append() calls taking much longer than other one

"""
# As Queues
""" 
-However ,lists are quite slow for this process because inserting and deleting an element at the beginning requires 
-shifting all of the other elements by one,requires o(n) time complexity.

"""









































