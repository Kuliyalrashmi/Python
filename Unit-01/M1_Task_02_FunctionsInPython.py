from re import X


def my_function1():
    print("Hello from function")
print("out of function")
my_function1()



# Function with one  parameter(python does not allow "int  + str")
def my_function2(fname):
    print(fname)
my_function2("rashmi")
my_function2(123)



#function with one or more parameters
def my_function3(fname,lname):
    print(fname+" "+lname)
my_function3("Email","password")
# my_function3(1,2)



#Arbitrary Arguments,*args     //for  n number of inputs parameter in function(make in a form of array/list/tuple)
def my_function4(*kids):
    print(kids[2])
my_function4("rashmi","kajal","chahak")
#my_function4("rashmi","kajal") #in this case the tuple index out of bond issue will occur
my_function4("rashmi",5,8,7.9)  #python is scripting lanuage since the statement above is getting error so this statemenet will not gets executed



#keyword argumrnts     
def my_function5(c1,c2,c3):
    print("the youngest child is:"+c2)
my_function5(c1="rashmi",c3="chahak" ,c2="kajal") 



#default argument
def my_function6(country="Norway"):
    print("i am from:"+country)
my_function6("India")
my_function6("Sweden")
my_function6()   #if we do not provide any argument then default argument will automatically pass  to the function
my_function6("canada")
 


# passing a list as an argument[iterator,object,list*]
def my_function7(food):
    for i in food:
        print(i)   #ITERATOR
fruits=["apple","banana","cherry",123,123,4]  #CREATION OF A LIST
my_function7(fruits)



#Returning values from a function
def my_function8(x):
    return 5*x
print(my_function8(3))
print(my_function8(5))
print(my_function8(9.4))



#pass function(when we need a function but we exactly do not know what we have to define inside a function then we use pass statement inside the function definition)
def my_function9():
    pass
my_function9()










