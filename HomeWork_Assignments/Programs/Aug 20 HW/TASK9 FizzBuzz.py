#Program to check Write a program that prints numbers from 1 to 100.
# Loop For However, for multiples of 3, print "Fizz" instead of the number, and
# for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5,
# print "FizzBuzz."

print("Its all about FizzBuzz\n")
for num in range(1,100):
    if num%3==0 and num%5!=0:
            print(f"Fizz - {num}\n")
    elif num%5==0 and num%3!=0:
        print(f"Buzz - {num}\n")
    elif num%5==0 and num%3==0:
        print(f"FizzBuzz - {num}\n")



