#1

n=int(input("enter the value of n"))
num = [i+1 for i in range(n)]
print(num)
num.insert(4,7)#add an item
print(num)
num.remove(1)#removing an item
print(num)
maximum=max(num)#store the max value
print(maximum)
minimum=min(num)
print(minimum)

#2

tuple1 = (1,2,3,4,5,)
newtuple1 = tuple(reversed(tuple1)) #reverse of tuple
print(newtuple1)


#3
tuple2 = ('c', 'h', 'a', 'r', 'i', 's', 'h', 'm', 'a')
newtuple2 = list(tuple2) #tuple into list
print(newtuple2)
