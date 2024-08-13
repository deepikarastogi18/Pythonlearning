#dynamically typed language
# at the run time data of the variable can be changed,and
# you don't need to mention the datatype

age=45
print(type(age))
age="deepika"
print(age)
print(type(age))

#long variable name
long_var_name_is_created_here="hello"
print(long_var_name_is_created_here)

a=b=c=10
sum=a+b+c
sum=sum-11
sum=sum+1
#this statement not storing the value only incrementing so value will remain 20
sum+1
print(sum)

#we can assign values by this way also
a,b,c=45,46,47
print(a,b,c,sep="_")