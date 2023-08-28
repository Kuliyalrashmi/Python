# question 1
#path='C:\\Users\\Rashmi Kuliyal\\OneDrive\\python_workspace\\Unit-03'
#path=path+'/'
import os
path=os.path.dirname(__file__)
print(path)
path=path+'/'
print(path)
def firstlinesFromAfile(file,nlines):
    data=file.readlines()
    length=len(data)
    print(str(data[:nlines:]))

file=open(path +"abc.txt","r")
#firstlinesFromAfile(file,3)


# Question 2
def lastlinesFromAfile(file,nlines):
    data=file.readlines()
    length=len(data)
    print(str(data[length-nlines::]))

# lastlinesFromAfile(file,2)

#Question 3

def longestWord(file):
    c=0
    data=[]
    data=file.read()
    s=data.split()
    print(s)
    for i in s:
        l1=len(i)
        if(l1>c):
            c=l1
    print(c)
    for i in s:
        if(len(i)==c):
            print(i)
#file.seek(0)
# longestWord(file)

# Second method of question 3  Using readlines() function
def longestWordsOfFile(file):
    allwords=[]
    data=file.readlines()
    for i in data:
        words=i.split()
        allwords=allwords+words
    maxlen=0
    for i in allwords:
        if(len(i)>maxlen):
            maxlen=len(i)
    for i in allwords:
        if(maxlen==len(i)):
            print(i)

# longestWordsOfFile(file)

#Question 4 
def OpenAfile(path,a):
    try:
        file=open(path +a,'r')
    except FileNotFoundError:
        print("Exception is handled")
        file=open(path+ a,'w+')
    return file

# file=OpenAfile(path, 'abcdef.txt')

print("hgmjhmkcldsnvkndvsldkmclsdbkcdsnklmls")
 
#Question 6
def uniqueWord(file):
    allwords=[]
    data=file.readlines()
    for i in data:
        words=i.split()
        allwords=allwords+words
    s=set(allwords)
    print(len(s))
uniqueWord(file)


