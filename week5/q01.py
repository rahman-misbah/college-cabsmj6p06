import math

# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Volume of cylinder
def volume_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

# Volume of cube
def volume_cube(side):
    return side ** 3

# Volume of cuboid
def volume_cuboid(length, breadth, height):
    return length * breadth * height

# Area of rectangle
def area_rectangle(length, breadth):
    return length * breadth

# Circumference of circle
def circumference_circle(radius):
    return 2 * math.pi * radius

# Main program
print('''Select an option:
1. Find the maximum of three numbers
2. Find Volume of Cylinder
3. Find Volume of Cube
4. Find Volume of Cuboid
5. Find Area of Rectangle
6. Find Circumference of Circle
7. Exchange Values of Two Variables
8. Find Distance Between Two Points''')
print()

option = int(input("Enter your choice (1-8): "))

match option:
    case 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        print("Maximum is:", max_of_three(a, b, c))
    
    case 2:
        radius = float(input("Enter radius of cylinder: "))
        height = float(input("Enter height of cylinder: "))
        print(f"Volume of Cylinder is: {volume_cylinder(radius, height):.2f}")
    
    case 3:
        side = float(input("Enter side of cube: "))
        print(f"Volume of Cube is: {volume_cube(side):.2f}")
    
    case 4:
        length = float(input("Enter length of cuboid: "))
        breadth = float(input("Enter breadth of cuboid: "))
        height = float(input("Enter height of cuboid: "))
        print(f"Volume of Cuboid is: {volume_cuboid(length, breadth, height):.2f}")
    
    case 5:
        length = float(input("Enter length of rectangle: "))
        breadth = float(input("Enter breadth of rectangle: "))
        print(f"Area of Rectangle is: {area_rectangle(length, breadth):.2f}")
    
    case 6:
        radius = float(input("Enter radius of circle: "))
        print(f"Circumference of Circle is: {circumference_circle(radius):.2f}")
    
    case 7:
        x = input("Enter value of first variable: ")
        y = input("Enter value of second variable: ")

        x, y = y, x

        print("After exchange, first variable:", x)
        print("After exchange, second variable:", y)
    
    case 8:
        x1 = float(input("Enter x-coordinate of first point: "))
        y1 = float(input("Enter y-coordinate of first point: "))
        x2 = float(input("Enter x-coordinate of second point: "))
        y2 = float(input("Enter y-coordinate of second point: "))

        distance = math.dist((x1, y1), (x2, y2))

        print(f"Distance between the two points is: {distance:.2f}")
    
    case _:
        print("Invalid option selected.")