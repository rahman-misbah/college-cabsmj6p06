r1 = int(input("Enter value of r1: "))
r2 = int(input("Enter value of r2: "))

if r2 <= r1:
    print("Error: r2 must be greater than r1.")
else:
    print(list(range(r1, r2 + 1)))
