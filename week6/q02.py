# Minimum number among three using if-else statements
def find_minimum(a: int, b: int, c: int) -> int:
    if a <= b and a <= c:
        return a
    elif b <= c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("The minimum value is:", find_minimum(a, b, c))