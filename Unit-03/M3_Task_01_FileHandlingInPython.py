# working of open() function
'''
Here file is a file object not a simple variable
file=open(filename with path,mode)

'''

# 1.Manual Approach to get file path
path='C:\\Users\\Manoj Kuliyal\\OneDrive\\python_workspace\\Unit-03'
path=path+'/'
file=open(path+'abc.txt','r')
for i in file:
    print("i:" ,i)
print("################################################################")
file.seek(0)  #it moves the file pointer to the beggining of the file
# print(file.read())  # it will give the output same as written in the file.
# print(file.read(8)) #Read eight characters from file including space and newline characters

# 2.OS.getcwd()
import os
path=os.getcwd()+'/Unit-03/'
print(path)

# 3. Another way to get path of the file
import os
path=os.path.dirname(__file__)
print(path)
path=path+'/'
print(path)

#4. Various Modes of opening a file
'''
r: just to read a file
w: open a file in write mode. if file does not exist it will make a new file if already present then it will overwrite the data.
a: open a file to append the data in file it appends the data after the data written in the file. it does  not override the data.
r+: to read and write data into the file. the previous data in the file will get overwrite.it does not create a new file if file is not present.
w+: we can read as well write into file(read+write(functionalities))
a+: we can read as well append the data into the file,it dioes not overwrite the data in the file

'''

# 5.Writing into the file
# file=open(path+"abc.txt","w+")
# file.write("12344")
# file.seek(0)
# file=open(path+"abc.txt","r")
# print(file.read())


# opening file in append+ mode
# file=open(path+"abcd.txt","a+")
# file.write("12344")
# file.seek(0)
# # file=open(path+"abc.txt","r")
# print(file.read())



# # opening file in append mode(we cant read in the file)
# file=open(path+"abc.txt","a")
# file.write("12344")
# # file.seek(0)
# # # file=open(path+"abc.txt","r")
# # print(file.read())

# #opening a file in r+ mode
# file=open(path+"abcd.txt","r+")  # it will throw an exception it cannot create a new file if does not exit
# print(file.read())


# #opening the  file in w+ mode
# file=open(path+"abc.txt","w+")
# file.write("12344")
# file.seek(0)
# # file=open(path+"abc.txt","r")
# print(file.read())

#rename a file
import os
path=os.path.dirname(__file__)
print(path)
path=path+'\\'
os.rename(path+"ABC.txt",path+"abc.txt")

"""
#Deleting a file(Case sensitive)
os.remove(path+"ABC.txt")
"""
file=open(path+"abc.txt",'r')
data=file.readlines()
print(type(data))
print(data)

for i in data:
    #print(type(i))#String
    words=i.split()
    #print(type(words))





