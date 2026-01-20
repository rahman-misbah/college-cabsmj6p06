# Area and type of triangle based on sides
def triangle_validity(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_area(a, b, c):
    if not triangle_validity(a, b, c):
        return None
    
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def triangle_type(a, b, c):
    if not triangle_validity(a, b, c):
        return None
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

area = triangle_area(a, b, c)
t_type = triangle_type(a, b, c)

if area is None or t_type is None:
    print("The given sides do not form a valid triangle.")
else:
    print(f"Area of the triangle: {area:.2f}")
    print(f"Type of the triangle: {t_type}")