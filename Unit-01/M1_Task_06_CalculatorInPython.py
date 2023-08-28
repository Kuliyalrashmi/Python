#CREATE A CALCULATOR IN PYTHON
#AND ALONG WITH THAT TEST ALL THE FUNCTIONALITIES
def add(x,y):
    #this will add the values of x and  y
    return x+y
def sub(x,y):
     #this will substract the values of x and y
    return x-y
def multi(x,y):
    #this will multiply the values of x and y
    return x*y
def div(x,y):
    #this will return the quotient in floating point number
    return x/y
def expo(x,y):
    #this will return the exponentiation of x in terms of y 
    return x**y
def floordiv(x,y):
    #this will return the value of quotient in integer form
    return x//y
def mod(x,y):
    #this will return the remainder of x divided by y .(it works on integers only)
    return x%y
def main():
    if add(5,2)==7:
        print("this function is working correctly")
    if sub(5,2)==3:
        print("this function is working correctly")
    if multi(5,2)==10:
        print("this function is working correctly")
    if div(5,2)==2.0:
        print("this function is working correctly")
    if expo(5,2)==25:
        print("this function is working correctly")
    if floordiv(5,2)==2:
        print("this function is working correctly")
    if mod(5,2)==1:
        print("this function is working correctly")
if __name__=="__main__":
    main()