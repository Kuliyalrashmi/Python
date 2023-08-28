# Exception,Error,Compilation issues
'''
1. Compilation uses:
  -Syntax issues,or issues in the code
  -catch by the python compiler
   pritn("kjdgfgdhj")
2. Exceptions:
  -Issues in your code, catch by PVM[Python Virtual Machine]
  -Run time issues , Handle[PVM]
    a=10
    b=0
    print(a/b)
  -Handeling is possible by using try and except
  -Exceptions are always handled by the programmer
3. Errors
   -Can not be handled by the programmer
   -Happen at run time
   -Even PVM can not catch them
   -Memory full ,stack overflow,power failure etc.
   -System design should be robust and Efficient
'''
mypath="C:\\Users\\Manoj Kuliyal\\OneDrive\\python_workspace\\Unit-03"
mypath=mypath+'/'
try:
    # we have to write sucpicious code in try block
    file=open( mypath +"abc.txt","w")
    file.write("321")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a/b
except ZeroDivisionError:
    #Handling of those exceptions
    print("b should not be 0")
    b=int(input("Enter b:"))
    c=a/b
else:
    print("Else block of code")
    print(c)
finally:
    #this block of code will always run 
    file.close()    
    print("file wiil get closed")
print(c)
print("hckdncekncn")
print("hckdncekncn")
print("hckdncekncn")
print("hckdncekncn")

#Raise an exception
x=int(input("Input X: "))
try:
  if x<0:
    raise Exception

except Exception:
  print("you should not take x negative")
  X=int(input("Insert X:"))
  # print("X: ",x)
  print("Hello World")
  print("Hello World")
  print("Hello World")
  print("Hello World")
else:
  print("X:",x)
finally:
  #Finally is used to close the files
  pass