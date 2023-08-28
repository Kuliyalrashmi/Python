# Notes
'''
-A Regex or Regular expression ,is a sequence of characters of characters that forms a search pattern.
-RegEx can be used to check if a string contains the specified search pattern.
-Python has a built-in package called "re", which can be used to work with Regular Expressions. 
'''
# txt="The rain in Spain"
# x=txt.find("ai") #This is not a RegEx function but a string function
# print(x)

# x=txt.find("ai",7)  # here 7 states that searching will start after 7 index
# print(x)


# import the re module:
import re
# txt="The rain in Spain"
# x=re.findall("ai",txt)
# print(x)   # findall returns all the instances of substring in th form of list
# x=re.findall("portugal",txt)   #it will return the empty list since portugal is not present in string txt
# print(x)

# #Search for the first whitespace character or even a word in the string
# txt="The rain in Spain,The rain in Spain"
# # x=re.search("\s",txt)
# # print(x)
# y=re.search("rain",txt)
# print(y.span())    # position of first occurence
# print(y.group())   # return the span of the words/Character
# print(y.start())   # it will read the string from start
# print(y.end())     # it will read the string from last

# # split a statement ,based on a single space
# txt="The rain in Spain"
# x=re.split("\s",txt)
# print(x)

# Control the number of occurences by specifying the  parameter
txt="The rain in Spain"
x=re.split("\s",txt,1) [0]  
print(x)

#return the string after split based on parameter
txt="The rain in Spain"
x=re.split("\s",txt,1) [1]  
print(x)

#The sub() function replaces the matches with the text of our choice(substitution)
txt="The rain in Spain"
x=re.sub("\s","_",txt)
print(x) 


#Match object
'''
-A match object is an object containing information about the search and the result.
-If there is no match ,the value None will be returned ,instead of the Match Object.
'''
# match object in RegEx
txt="The rain in Spain"
x=re.search("ai",txt)
print(x)
print(type(x))
print(x.start())  # it will return the starting index of span
print(x.span())   
print(x.group())
print(x.end())    # it will return the ending index of span


############################### Questions ###############################
# Q1. Find host or domain name from text provided
# 1. First Approach(string name)
data='From rashmikuliyal@gmail.com 12-12-2022 09:14:16'
ind1=data.find("@")
print(ind1) #18
ind2=data.find(" ",ind1)
print(ind2) #28
print(data[ind1+1:ind2+1])

#2.Second Approach( using RegEx)
# print(re.search("@.*",data).group().split()[0])
x=re.search("@.*",data)
print(x)
x=x.group()
print(x)
x=x.split()[0]
print(x)

#Q2 Extract Date from a String
txt="I have submitted my report to the department on 12.12.2022,12122022"
x=re.search("([0-9]{2}\.[0-9]{2}\.[0-9]{4})",txt)
print(x.group())


#Q3 Return All the words of a string that starts with vowel
txt="I have submitted my report to the department on 12-12-2022,12122022"
print(re.findall("\\b[aeiouAEIOU]\S*",txt)) # enumerate all the world in a string to extract all the world in a string   S(it denotes non space characters)
# d=for digits
# D=for non-digits

#Q4 split the string with multiple delimeters
txt="I have submitted my report to the department on 12-12-2022,12122022"
print(re.split("\s|,|\.",txt))


#Q5 Return the first word of a given string
txt="I have submitted my report to the department on 12-12-2022,1
2122022"
# x=txt.split(" ")[0]   using the method of string
# print(x)
print(re.split("\s",txt)[0])   #using regex


#Q6 Return all the words of a string
txt="I have submitted my report to the department on 12-12-2022,12122022"
print(re.split("\s",txt))
6