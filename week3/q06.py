# Exchange values using XOR

a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))

# Swap
a = a ^ b   # a = a ^ b
b = a ^ b   # b = a ^ b ^ b = a
a = a ^ b   # a = a ^ b ^ a = b

print("After swapping:")
print("First integer (a):", a)
print("Second integer (b):", b)