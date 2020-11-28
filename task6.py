#1.

before_list=[1,2,3,4,5,]
print("List before addition",before_list)
after_list=[]
for i in range(0,len(before_list)):
    after_list.append(before_list[i]+2)
print("List after addition",after_list)
print()

#2.
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end='')
    print()

#3.

n=int(input("Enter the terms"))
f1=0
f2=1
if n<=0:
    print("Fibbonacci series",f1)
else:
    print(f1,f2,end=" ")
    for x in range(2,n):
        f0=f1+f2
        print(f0,end=" ")
        f1=f2
        f2=f0
print()

#4.
#AMRSTRONG NUMBER: if a number  equal to the sum of the cubes of its own digits,then it is called armstrong number
#example: 370 = 3*3*3+7*7*7+0*0*0

n=int(input("Enter a number: "))
sum=0
x=n
while (x>0):
   digit=x%10
   sum+=digit**3
   x//=10
if (n==sum):
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
print()

#5.
n=9
print("Multiplication table of 9")
for i in range(1, 11):
   print(n,'x',i,'=',n*i)
print()

#6.

a=int(input("enter a number"))
if(a<0):
    print(a,"is a  negative number")
else:
    print(a,"is a positive number")
print()
#7.

d=int(input("enter the days"))
age=(d/365)
print("Age: ",age,"years")
print()

#8.


import math
x=int(input("enter a value"))
print("math.sin(",x,"): ",math.sin(x));
print("math.cos(",x,"): ",math.cos(x));
print("math.tan(",x,"): ",math.tan(x));
print()

#9.

print("Simple calculator")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
select=input("select operations +,-,*,/,%")
if(select=='+'):
    sum=n1+n2
    print("Addition operation ",sum)
elif(select=='-'):
    sub=n1-n2
    print("Subraction operation ",sub)
elif(select=='*'):
    mul=n1*n2
    print("Multiplication operation ",mul)
elif(select=='/'):
    div=n1/n2
    print("Divison operation ",div)
elif(select=='%'):
    quotient=n1%n2
    print("Quotient ",quotient)
else:
    print("Select a desired operation")