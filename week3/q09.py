# Factorial using loops

x = int(input("Enter a non-negative integer: "))

if x < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, x + 1):
        factorial *= i
        
    print(f"The factorial of {x} is: {factorial}")