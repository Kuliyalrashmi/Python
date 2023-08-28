# #sys.argv
# '''
# sys.argv: Command line arguments:
# - Command line arguments are those which are passed during the calling of the program along wiith the calling statement.
# '''

import sys

# #total arguments
# n=len(sys.argv)
# print("Total arguments passed:",n)

# #Arguments passed
# print("\nName of Python script:",sys.argv[0])


# print("\nArguments passed:",end=" ")
# for i in range(1,n):
#     print(sys.argv[i],end=" ")

# #Addition of numbers
# Sum=0
# for i in range(1,n):
#     Sum+=int(sys.argv[i])

# print("\n\nResult:",Sum)
import math
def primeornot(n):
    value=math.ceil(math.sqrt(n))
    for i in range(2,value+1):
        if n%i==0:
            return "Not Prime"
    return "Prime"
result=primeornot(int(sys.argv[1]))
print(result)