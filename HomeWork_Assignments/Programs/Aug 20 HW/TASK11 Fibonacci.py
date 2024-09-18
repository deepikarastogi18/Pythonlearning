#Program to print fibonacci series

num=int(input("Enter the number\n"))
j = 0
k=1
print(f"Fibonacci series is {j}\n")
for i in range(0,num+1):
    fibo=j+k
    print(f"Fibonacci series is {fibo}\n")
    j=k
    k=fibo

