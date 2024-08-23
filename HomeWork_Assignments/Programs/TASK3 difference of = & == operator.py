#Program to show difference between = and == operator

# = operator working as an assignment operator,assigning literal value on the right to the identifier on the left
EmpId=101
print(EmpId)

num1=int(input("Enter value of first number\n"))
num2=int(input("Enter value of second number\n"))
if num1==num2:
    print("Both numbers are same")
else:
    print("Numbers are different", num1,num2)


