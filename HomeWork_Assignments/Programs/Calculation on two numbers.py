#Perform various maths operations on two numbers

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

#Calculate addition of two numbers
sum=num1+num2

#Calculate substraction of two numbers
sub=num1-num2

#Calculate multiplication of two numbers
mul=num1*num2

#Calculate division of two numbers
div=num1/num2

#Calculate power of two numbers
power=pow(num1,num2)

#Calculate maximum among two numbers
maxi=max(num1,num2)

#Calculate minimum among two numbers
mini=min(num1,num2)

#output
print("Addition of two numbers is " f"{sum}")
print("Subtraction of two numbers is " f"{sub}")
print("Multiplication of two numbers is " f"{mul}")
print("Division of two numbers is " f"{div}")
print("Power of two numbers is " f"{power}")
print("Maximum among two numbers is " f"{maxi}")
print("Minimum among two numbers is " f"{mini}")


