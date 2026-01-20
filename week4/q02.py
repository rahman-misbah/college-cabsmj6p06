from math import pi

def sphere_volume(radius : float) -> float:
    return 4 / 3 * pi * radius**3

radius = float(input("Enter radius of sphere: "))

if radius < 0:
    print(f"Invalid input {radius}")
else:
    print(f"Volume: {sphere_volume(radius):.3f}")