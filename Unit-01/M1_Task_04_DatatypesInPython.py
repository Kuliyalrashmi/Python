#variable is like a container
var1=123
var2=123.4
var3="Hello"
print(var1)
print(var2)
print(var3)

#Casting of a value
x=str(321)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)
#python string/character storage
# Double quote and single Quote 
x="john"
x='john'
x="b"
x='b'
x="""abc"""
x='''abc'''
print(x)

#type of variable
var1=123
var2=123.4
var3="Hello"
print(type(var1))
print(type(var2))
print(type(var3))
print("Hello World\n"*10)
print(10*5)

#Data Types
'''
1-Numeric:
    int
    float
2-Binary ,Octal,and Hexadecimal:
    n1=0B0101010   #[0B for Binary{0,1}]
    n2=0O17        #[0O for Octal{0,1,2,3,4,5,6,7}]
    n3=0X1c2       #[0X for Hexadecimal{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}]
3 Bool Data Type:3
    a=10
    b=20
    if(a<b):print("HELLO")
'''
#Binary Octal And HexaDecimal
n1=0B0101010   
n2=0O17        
n3=0X1c2 
print(n1)
print(n2)
print(n3)

#Bool Data Type
a=10
b=20
if(a<b):print("HELLO")


#Another way to convert binary,octal and hexadecimal to decimal number
print(int('0101010',2))
print(int('17',8))
print(int('1c2',16))
 