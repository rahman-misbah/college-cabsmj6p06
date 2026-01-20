length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

surface_area = 2 * (length * breadth + breadth * height + height * length)
volume = length * breadth * height

print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")