#1.
print("1.Merge two lists intpo tuple using zip()")
print("------------------------------------------")
list1 = [1,2,3]
list2 = ['a','b','c']
print(tuple(zip(list1, list2)))
print()

#2.
print("2.Create range from 1 to 8.Then zip,merge the 2 lists into tuple")
print("----------------------------------------------------------------")
def list1(r1, r2):
    return list(range(r1, r2+1))
r1, r2 = 1, 8
print("Created list using range:")
print(list1(r1, r2))
list2=[2,3,4,5,6,7,8,9]
print("Two lists after merging into a tuple")
print(tuple(zip(list1(r1,r2),list2)))
print()

#3.
print("3.using sorted function(),sort the list in ascending order")
print("-----------------------------------------------------------")
list_values= ['r','s','c','a','g','w']
print("Given list of values are",list_values)
sort_asc = sorted(list_values)
print("Sorted list : ",sort_asc)
print()

#4.
print("4.Using filter() function,print only odd numbers into a new list")
print("-----------------------------------------------------------------")
list4 = [1,2,3,4,5,6,7,8,9,10]
print("Given list :",list4)
odd=[]
x=lambda n: n%2!=0
odd=list(filter(x, list4))
print("Odd numbers in the list are :",odd)
