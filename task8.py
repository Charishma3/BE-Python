#1.types of errors

print("1.LIST OF ERRORS")
print(dir(locals()['__builtins__']))
print()
print("ERRORS WITH A SAMPLE PROGRAM USING TRY AND EXCEPT")
#Arithematic error
try:
    a = 10/0
    print (a)
except ArithmeticError:
        print ("1.Arithematic error")
#index error
try:
    list1=[1,2,3]
    print(list1[4])
except IndexError:
    print("2.IndexError")
#KeyError
try:
    array = {'a': 1, 'b': 2}
    print(array['c'])
except KeyError:
    print("3.KeyError")
#NameError
try:
    def func():
        print(ans)
    func()
except NameError:
    print("4.NameError")

#TypeError
try:
    arr = ('tuple',) + 'string'
    print(arr)
except:
    print("5.TypeError")

#ValueError
try:
    print(int('c'))
except ValueError:
    print("6.ValueError")
#ZeroDivisionError
try:
    print(1/0)
except ZeroDivisionError:
    print("7.ZeroDivisionError")
print("---------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------

#2.Calculator
print("2.SIMPLE CALCULATOR")
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
print("Select operation.")
print("+")
print("-")
print("*")
print("/")
select = input("Enter choice(+/-/*//): ")
num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
try:
    if select == '+':
        print(num1,"+",num2,"=",add(num1, num2))
    elif select == '-':
        print(num1,"-",num2,"=",subtract(num1, num2))
    elif select == '*':
        print(num1,"*",num2,"=",multiply(num1, num2))
    elif select == '/':
        print(num1,"/",num2,"=",divide(num1, num2))
    else:
        print("Invalid selection")
except Exception as e:
    s=str(e)
    print("Error: {}".format(s))
print("------------------------------------------------------------------------------------------")


#-------------------------------------------------------------------------------------------------

#3.
print("3.TRY BLOCK RAISES A NAMEERROR")
try:
    print(hello)
except NameError:
    print("Variable hello is not defined")
except:
    print("Some error occured!Please check.....")
finally:
    print("try and except block finished")
print("---------------------------------------------------------------------------------------------")

#4.
print("4.WHEN TRY EXCEPT IS NOT REQUIRED")
print("When you dont have exceptions or errors,it is actually better to let the problem reveal, rather than hiding it.")
print("-----------------------------------------------------------------------------------------------")
print()
#5.
print("5.INPUT INSIDE TRY EXCEPT BLOCK")
try:
    x = int(input("Enter an integer: "))
    print("Your number was", x)
except (TypeError, ValueError):
    print("Sorry,That was not an integer.")

