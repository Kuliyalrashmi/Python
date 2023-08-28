import re
txt="Hey this is Rashmi Kuliyal,Software Engineer,rashmikuliyal@122347gmail.com Rashmi 11292327"
#. and / regex
result=re.search("\.",txt)   # . is used to find for particular character it is reserved character in RegEx
print(result.start())        # \ is escape sequence used to escape the character is used when we want to use the reserved symbols as normal symbols

# #@.*Regex
result=re.search("@.*",txt)  # it will return all the characters present in string after the symbol(@. means to return the character just after the @ symbol)
print(result.group())        # only @ as parameter means 


result=re.search("@\d",txt)  # it is used to find the digits in string after the @ sign
print(result.group())

#[ ]= it defines the range of characters from where it have to find
#{}= it defines how manywerfff times we have to find the digits
result=re.search("@\d*",txt) # *(zero or more)it is optional that the character that we are finding it is optional to find the desired character
print(result.group())
result=re.search("@\d+",txt) # +(atleast 1 or more) means if i am finding anything(digit) then that (digit) atleast should present after the @
print(result.group())

result=re.search("@",txt)  # it will Simply search the particular character 
print(result.group())

########################## EXTRACTION OF DATE #####################
txt="I have submitted my report to the department on 12-12-2022,12122022"
x=re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})",txt)  #{2} IT IS USED TO FIND OUT THE NUMBER OF DIGITS WE HAVE TO FIND
print(x.group())

txt="12234455hjdgjgdh"
print(re.findall("4\d",txt)) # if we use findall to find anything in the string if it does not find anything then it returns none(returns list)
                             # and in the case of search it will break the code
print(re.findall("7\A",txt)) #it means if the strating character of the string is 1


txt="a234455 2222 12"
print(re.findall("a?",txt)) #it will return whether a is present or not



import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("e?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
