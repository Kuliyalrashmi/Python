# OS and SYS Modules

import os
import sys

# get the current working directory(CWD)
cwd=os.getcwd()
print("Current working directory:",cwd)

#Changing the current working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

current_path()

# Changing thw CWD
os.chdir('../')
#printing CWD after change
current_path()

#make Your Own directory
directory="rashmi"
parent_dir=os.getcwd()
path=os.path.join(parent_dir,directory)
# os.mkdir(path)

#Remove a file
file="odoj.txt"
path=os.path.join(parent_dir,file)
# os.remove(path)

#Removing Dir.[Dont't run in Source Code folder]
#directory="rashmi"
#path=os.path.join(parent_dir,directory)
#os.rmdir(path)

################## SYS MODULE#########################
'''

The syd module in python provides various functions and variables that are used to manipulate different parts of the python runtime environment.

-----sys.version is used which returns a string containing the version of Python Interpreter with some additional information.
-----This shows how the sys module interacts with the interpreter.

'''
import sys 
print(sys.version)


#input and output 

#  stdin:
#----- It can be used to get input from the command line directly.
#-----It also,automatically adds '\n' after each sentence
import sys
for line in sys.stdin:
    if 'q'==line.rstrip():
        break
    print(f'Input :{line}')

print("Exit")


# stdout:
'''----- A built-in file object that is analogous to the interpreter's
     standard output stream in python.
------ stdout is used to display output directly to the screen console.
'''

import sys
sys.stdout.write("Rashmi Kuliyal")
sys.stdout.write("Rashmi Kuliyal")
sys.stdout.write("Rashmi Kuliyal")
sys.stdout.write("Rashmi Kuliyal")
sys.stdout.write("Rashmi Kuliyal")
sys.stdout.write("Rashmi Kuliyal")
# By default print statement has new line character But in write function there is a white space character

#end=" "
"""
-By Default,the Print function ends with a newline.
-Passing the whitespace to the end parameter(end=' ') indicates that the end character has to be identified by whitespaces and not a newline
"""


#Q1.
"""
Wap in Python to check if the entered number is prome or not using coomand line argument technique
Also use square root  technique to check if it is prime or not
"""

import math
def primeornot(l):
    value=math.ceil(math.sqrt(l))
    for i in range(2,value+1):
        if l%i==0:
            return "Not Prime"
    return "Prime"
result=primeornot(sys.argv[0])
print(result)