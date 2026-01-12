x = float(input("Enter x: "))
y = float(input("Enter y: "))

term_1 = 1 + x/y + x**y
term_2 = 2 + y/x + y**x
result = term_1 * term_2

print(result)