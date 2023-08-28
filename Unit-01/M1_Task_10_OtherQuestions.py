#Q.1
s="H2O"
script=str.maketrans("0123456789","₀₁₂₃₄₅₆₇₈₉")
p=s.translate(script)
print(p)

#Q.2
x=int(input("enter the marks: "))
if(x<30):
    print("fail")
elif(x==30):
    print("Pass But bad score")
elif x>=40 and x<50:
    print("OK")
elif x>=50 and x<60:
    print("OK OK")
elif x>=60 and x<75:
    print("First Class")
elif x>=75:
    print('First class With "D"')





