x=int(input("please enter an integer:"))


#if else statement
if x<0:
    print("less than zero")
elif x==0:
    print("equals to Zero")
elif x==1:
    print("single")
else:
    print("More")

#for statements in python(The range() function)
for i in range(1,5):
    print(i)


x=5
#while loop in python
print("values in reverse order")
while(x>=1):
    print(x)
    x=x-1

#break and continue statemnet in python and else clauses in python
n=7
count=0
for x in range(2,n):
    if n % x==0:
        print("Not a prime")
        count=count+1
        break
    else:
        continue
if count==0:
    print("it is a prime number")

#the pass statement

def initlog():
    pass  #remember to implement this
initlog()

#match statements 
cpuModel=str.lower(input("please enter your cpu model: " ))
match cpuModel:
    case "celeron":
        print("forgrt about it and play minesweeper instead.....")
    case "core i3":
        print("good luck with that")
    case "i5":
        print("you should be fine")
    case "core i7":
        print("have fun")
    case "core i9":
        print("we have a new thing for you")
    case _ :
        print("is that even a thing")

#Short Circuit (lazy Evaluation) (minimal evaluation)
"""
When evaluating an expression that involves the or operator python can sometimes determine the result without evaluation of all the operands.
this is called short-circuit evaluation or lazy evaluation. 

"""
