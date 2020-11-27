#1.aritematic operations using functions

num1=int(input("First number: "))
num2=int(input("second number:"))
def arithematic(a,b): #function for arithematic operations
    sum=a+b;
    print("sum: ",sum)
    difference=a-b;
    print("difference: ",difference)
    product=a*b;
    print("product: ",product)
    division=a/b;
    print("division:",division)
arithematic(num1,num2)

#2
name1 = input("enter the patient name:")
def covid(name,temp=98):
    print("Patient name is ",name,"and the body temperature is ",temp,"degrees")
covid(name1)