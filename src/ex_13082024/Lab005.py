#Calculate the division
Division=100/50
print("Division is",Division)
#division will give result in float as python is smart language,it understand most of the result can give remainder


#we can also format the value of division till the decimal points we want
#it will round of if next num from 4 is greater than 5 it will round off as per maths
Formated_division=f"{Division:.4f}"
print(Formated_division)

#formating is also used to print the output in specific way

num=50
print("This is the way to show the number " f"{num}")

#We can also use formatting to print table of number
print("Table of 9 is:")
no=9
print(f"{no}*1=",no*1)
print(f"{no}*2=",no*2)
print(f"{no}*3=",no*3)
print(f"{no}*4=",no*4)