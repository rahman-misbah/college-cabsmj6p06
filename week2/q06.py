# ax^5 + bx^4 + cx^3 + dx^2 + ex + f^(1/2)
a = 3
b = -2
c = 6
d = 1
e = 4
f = 7

x = int(input("Enter the value of x: "))

ans = a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f**0.5

print(ans)