from math import tan, pi
sides = int(input("enter the no of sides: "))
length = float(input("enter the length : "))
area = sides * (length ** 2) / (4 * tan(pi / sides))
print("The area of the polygon is: ",area)
