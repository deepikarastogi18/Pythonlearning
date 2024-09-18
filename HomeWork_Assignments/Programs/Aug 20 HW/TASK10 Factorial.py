#Program to find factorial of a number

num=int(input("Enter the number\n"))
for i in range(1,num):
    num=num*i
print(f"Factorial of number {num}")