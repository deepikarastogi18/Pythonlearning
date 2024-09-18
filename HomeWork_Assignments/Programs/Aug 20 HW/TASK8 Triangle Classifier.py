#Program to check whether triangle is equilateral, isosceles or scalene

Side1=int(input("Enter first side of triangle\n"))
Side2=int(input("Enter second side of triangle\n"))
Side3=int(input("Enter third side of triangle\n"))

if Side1==Side2==Side3:
  print("Triangle is equilateral triangle")
elif Side1==Side2 or Side2==Side3 or Side1==Side3:
    print("Triangle is isosceles triangle")
else:
  print("Triangle is scalene")