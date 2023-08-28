#  nameError: name 'george' is not defined
#  >>> "george"
#  'george'
#  >>> 'george'
#  'george'
#  >>> '''george'''
#  'george'
#  >>>
#  >>> """george"""
#  'george'
#  >>> george
#  Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#  NameError: name 'george' is not defined
#  >>> 'george'
# Escape a character
#  print('I\'m fine')
#  print('press "enter"')
#  'Red'  'Car'
#  print('red'+ ' ' + 'car')
#  >>> 'I\'m fine'
#  "I'm fine"
#  >>> 'press"enter"
#    File "<stdin>", line 1
#     'press"enter"
#   
#  SyntaxError: unterminated string literal (detected at line 1)
#  >>> 'press"enter"'
#  'press"enter"'
#  >>>
# print('red', 'car')
# >> string="A string"
# >>> string[0]
# 'A'
# >>> string[0:2]
# 'A '
# >>> string[0:3]
# 'A s'
# >>> string[1:4:1]
# ' st'
# >>> string[2::]
# 'string'
# >>> string[-4:-1]
# 'rin'
# >>> string[::]
# 'A string'
# >>> string[::2]
# 'Asrn'
# >>> string[-1:-4:-1]
# 'gni'
# >>> ("string")*10
# 'stringstringstringstringstringstringstringstringstringstring'
# >>> ("string ")*10
# 'string string string string string string string string string string '
# >>> "rashmi"
# 'rashmi'
# >>> 'rashmi'
# 'rashmi'
# >>> '''rashmi'''
# 'rashmi'
# >>>
#compare two strings
s1="hello"
s2="pooja"
if s1==s2:
    print("Equals")
else:
    print("Not Equals")
if s1<s2:
    print("s1 is smaller than  s2")
else:
    print("s2 is smaller than s1")

    
#Remove Spaces from string
name=" rashmi kuliyal "
print(name.rstrip())  #remove spaces from right side
print(name.lstrip())  #remove spaces from left side
print(name.strip())   #remove spaces from both sides
print(name)


#find a substring
str=input("enter main string: ")
substr=input("enter sub string: ")
n=str.find(substr,0,len(str))
if n==-1:
    print("substring not found")
else:
    print("substring found at position",n)

#string are immutable in python:'
'''
An immutable object is a object whose content can not be changed in python python : strings, numbers and tuples are mutable
'''
s1='one'
s2='two'
s1=s2
print(s1)

# Replace a substring 
str="that is beautiful"
s1="beautiful"
s2="not beautiful"
str1=str.replace(s1,s2)
print(str1)

#split function
str="that is beautiful"
str1=str.split()  # split() split the string by spaces and store them into list as list items
print(str1)
for i in str1:
    print(i)

#changing case of the string
str1="That is beautiful"
print(str1.upper())
print(str1.lower())

#supercript and subsript in python
numbers_to_letter=str.maketrans("123","ABC")
print("Question 1, point 2 and 4".translate(numbers_to_letter))

subscript=str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("C2H5OH".translate(subscript))

superscript=str.maketrans("0123456789","⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript))


superscript=str.maketrans("0123456789","⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript).replace("PI","π"))


