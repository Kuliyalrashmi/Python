#Q.1
lst=[1,2,3,"A","HELLO",123.5,4,5,6,7,8,9]
sum=0
for i in lst:
    if type(i)==int:
        sum=sum+i
print(sum)

#Q.2
lst=["Hey this is Amit","Hey this is Amit","Hey this is Amit","Hey this is Amit" ]
K="A"
result=[]
for i in lst:
    l=i.split()
    for j in l:
        if j[0].lower()==K.lower():
            result.append(j)
print(result)


#Q.3
list=["Hey this is Amit","Hey this is Amit","Hey this is Amit","Hey this is Amit" ]
k="t"
result=[]
for i in list:
    l=i.split(k)
    result=result+l
print(result)

#Q.4
s="However, Ram has been in the news for all the wrong reasons too.Illiterate bigots have weaponized the slogan Jai Shri Ram forwanton acts of violence, crime and hatred, which are anathema towhat Ram actually stands for. These lumpen elements do not knowthat Ram is maryada purushottam, the epitome of rectitude, thetouchstone of impeccable behaviour, the role model of the perfecthuman being, and the very incarnation of saumya rasa, harmoniousequilibrium"
l=s.split(" ")
print(l)
count=0
for i in l:
    if(i=="Ram" or i=="Ram."):
        count=count+1
print(count)
n=l.count('Ram')
print(n)

#Q.5
s1=s.replace('Ram','Shree Ram')
print(s1)
print()
print()

#Q.6
lst=s1.split(" ")
lst.sort(reverse=True)
strng=""
for i in lst:
    strng=strng+i+" "
# print(strng)
s3=strng.rstrip()
print(s3)

# s4=strng(lst)
# print(s4)
# print(s4[0])

#Q.7
arr=[1,2,3,4,5,7,6]
temp=arr.copy()
# temp=arr[:]
temp.sort()
print(temp)
print(arr)
if(arr==temp):
    print("List is sorted")
else:
    print("Not Sorted")


