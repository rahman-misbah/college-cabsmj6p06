# Swap using addition and subtraction

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b   # a = a + b
b = a - b   # b = a + b - b -> b = a
a = a - b   # a = a + b - a -> a = b

print(f"First Number: {a}, Second Number: {b}")