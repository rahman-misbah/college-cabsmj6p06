x = int(input("Enter x: "))
y = int(input("Enter y: "))

ans = (1 + x / y + x**y) / (2 + y / x + y**x)

print(ans)