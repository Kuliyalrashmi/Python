import math
def primeOrNor1(a):
    count=0
    for i in range(2,a):
        if(a%i==0):
            count=1
            break

    if(count==0):
        print("Number is prime")
    else:
        print("Number is not Prime")
def primeOrNor2(a):
    count=0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            count=1
            break

    if(count==0):
        print("Number is prime")
    else:
        print("Number is not Prime")
def primeOrNor3(a):
    count=0
    y=int(math.sqrt(a))
    for i in range(2,y+1):
        if(a%i==0):
            count=1
            break

    if(count==0):
        print("Number is prime")
    else:
        print("Number is not Prime")

def sqrt1(a):
    i=1
    while(i*i<=a):
        i=i+1
    return (i-1)
    
def primeOrNor4(a):
    count=0
    y=int(sqrt1(a))
    for i in range(2,(y+1)):
        if(a%i==0):
            count=1
            break

    if(count==0):
        print("Number is prime")
    else:
        print("Number is not Prime")

x=int(input("enter a number:"))
#primeOrNor1(x)
# primeOrNor2(x)
# primeOrNor3(x)
primeOrNor4(x)