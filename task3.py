#1.merge two python dictionaries
dict1 = {'apple':2,'mango':3,'orange':5}
dict2 = {'fruits':3,'total':10}
dict1.update(dict2)
print(dict1)

#2.remove a key from a dictionary
d = {'one':1,'two':2,'three':3,'four':4}
del d['four']
print(d)

#3.map two lists into a dictionary
a = ["name", "regno", "dept" ]
b = ["charishma", 4069, "cse"]
c = {k: v for k, v in zip(a, b)}
print(c)

#4.find length of a set
seta = set( )
seta.add("charishma")
seta.add(4069)
seta.add("cse")
seta.add("3 year")
print(len(seta))

#5.remove intersection of a 2nd set from the 1st set
s1 = {'a','b','c','d','e'}
s2 = {1,2,3,4,5}
print(s1)
print(s2)
print("after remove operation",s1-s2)

