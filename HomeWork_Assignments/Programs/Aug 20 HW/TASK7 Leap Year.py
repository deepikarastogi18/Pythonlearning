#Program to check year is leap year or not

year=int(input("Enter the year\n"))
#logic to check leap year
if year%4==0 and year%100 !=0:
    print(f"{year} is a leap year\n")
elif year%400==0 and year%100==0:
    print(f"{year} is a leap year\n")
else:
    print(f"{year} is not a leap year")