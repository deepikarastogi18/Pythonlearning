#Program to compare two numbers
num1 = int(input(" Enter first number\n"))
num2 = int(input(" Enter second number\n"))
if num1>num2:
    print(f"Greater number is {num1}")
    print(f"Smaller number is {num2}")
elif num1<num2:
    print(f"Greater number is {num2}")
    print(f"Smaller number is {num1}")
else:
    print("Both numbers are equal")
