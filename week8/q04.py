# Generate tuples of (i, 5 * i**3) for a given range

n = int(input("Enter value of n: "))
data = [(i, 5 * i**3) for i in range(n+1)]

print("Result:", data)