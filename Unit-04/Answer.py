import re
# Q1 write a python program to find out all the words that  ends with  a vowel
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh"
print(re.findall("\S*[aeiouAEIOU]\\b",txt))

# Q2 write a python program to find out all the words start with a digit.
txt="123rashmi 767kuliyal yujjbbj"
print(re.findall("\\b[0-9]\S*",txt))

# Q3. write a python program to fetch the date from a string and make sure out of range date should not be fetched.
txt="I have submitted my report to the department on 12.12.2022,12122022,40.34.2022"
x=re.search("([0-2][0-9]\.[0-1][0-2]\.[0-9]{4})",txt)
print(x.group())

#Q4. write a python program to fetch all the words which starts with a capital letter.
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh"
print(re.findall("\\b[A-Z]\S*",txt))

#Q5. write a python program that matches a string that has an a followed by either [A-Z] , [a-z] or [0-9]
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh a87889"
x=re.search("a\w*",txt)
print(x)
y=re.findall("a\w*",txt)
print(y)

#Q6. write a python program to search a string which start with y or Y or z or Z
txt="Rashmi Yjscgd Zhjdgf zhbj ykdb kuliyal"
y=re.search("\\b[ZzYy]\S*",txt)
print(y)
x=re.findall("\\b[ZzYy]\S*",txt)
print(x)

# q.7 Write a python program to fetch all the words from string 
# which do not contatin any special character
txt="Rashmi Yjscgd Zhjdgf zhbj ykdb kuliyal adls@nf enknf$"
x=re.findall("^\w*",txt)
print(x)
#Q.8 Write a python program to fetch all the special symbols from a string

# Q.9 write a python program to fetch all the words which contain only alphabets and should be of size of 3
x=re.findall("\\b[A-Za-z]{3}\s",txt)
print(x)