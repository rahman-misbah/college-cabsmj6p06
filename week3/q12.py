# hcf
def hcf(x, y):
    if x < 0 or y < 0:
        return -1
    
    while(y):
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = hcf(num1, num2)

if result == -1:
    print("Please enter non-negative integers only.")
else:
    print(f"The HCF of {num1} and {num2} is {result}")