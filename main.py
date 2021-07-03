#number1
n=int(input("distance1"))
m=int(input("distance2"))
print(m/n)




#number2
n=int(input("number"))
c=n%10
n=n//10
b=n%10
a=n//10
print(a+b+c)




#number3
a=int(input("number1"))
b=int(input("number2"))
c=int(input("number3"))
d=a
if d<b:
    d=b
if d<c:
    d=c
print(d)




#number4
a=int(input("год"))
if a%4==0 or (a%100==0 and a%400==0):
    print("высокосный")
else:
    print("обычный")




#number5
a=int(input("число"))
if a%2==0:
    print("четное")
else:
    print("нечетное")
