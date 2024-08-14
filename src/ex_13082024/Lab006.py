#String functions

name="Deepika"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a="100"
print(type(a)) #this is string
age=10
print(type(age))#this is int

line="This is a big line "
print(type(line))
#line=line+1 #this will throw error as int is copared with string
line=line+"1"
line=line+str(1)
#above lines will concatenate the string
print(line)

How_many_planes_I_have=None #this is None type
print(type(How_many_planes_I_have))
#null is not resent in python

val=0 #this is int ,we can assign 0 to variable

#id of object

age=10
age2=10
print(id(age))
print(id(age2))#if value is same for both variable it will point to same address to save memory
#python is samrt enough to arrange a memory to make best use
age3=11
print(id(age3))

