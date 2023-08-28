#Lambda or anonymous functions in python
'''
-A lambda function is a small anonymous function
-A lambda function can take any number of arguments
-It can create functions in one line when possible

'''
import math 
def add(a,b):
    return a+b

def minus(x,y):
    return x-y-2


minus=lambda x,y: x-y
print(minus(9,4))

#Q2.
'''
WAP in Python to calculate the square root of a whole number by using lambda expression and math.sqrt technique
'''
square=lambda x: math.sqrt(x)
print(int(square(9)))

# MAp In Python
'''
-The map() function executes a specified function for each item
-The item is send to the function as a parameter
'''
def myfunc(n):
    return len(n)
# a1=myfunc("cat")
# a2=myfunc("dog")
# a3=myfunc("goat")
# a4=myfunc("rabbit")
# a5=myfunc("tiger")
# print(a1,a2,a3,a4,a5)
result=map(myfunc,("cat","dog","rabbit","goat"))
print(list(result)[2])

def myfunc1(a,b):
    return a+b
x=map(myfunc1,('apple','banana'),('orange','lemon','pineapple'))
print(list(x))

#Q4 Wap in python to check if the number is prime or nor? check multiple numbers at once
def primeornot(n):
    value=math.ceil(math.sqrt(n))
    for i in range(2,value+1):
        if n%i==0:
            return "Not Prime"
    return "Prime"
x=map(primeornot,(7,8,9,10,12,18,56,19,17))  #map function returns map object
print(list(x))