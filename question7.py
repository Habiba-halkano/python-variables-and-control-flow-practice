#python program that takes 3 sides of a triangle and determines whether the triangle is:
# equilateral(all sides equal),isosceles (two sides equal) or scalene(all sides different)

#function definition
def triangle_sides(side1, side2, side3):
    if side1 == side2 and side1 == side3:
        print("Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")

#prompt user to input sides
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

#function call
triangle_sides(side1, side2, side3)
