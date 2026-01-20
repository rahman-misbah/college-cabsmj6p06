# Addition using bitwise operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    carry = a & b
    a = a ^ b   # a stores sum without carry

    b = carry << 1  # b stores carry for the next iteration

print(f"The sum is: {a}")