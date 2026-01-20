def factorial(n : int) -> int:
    if n < 0: raise ValueError("n cannot be negative")
    
    result = 1

    for i in range(1, n + 1): result *= i

    return result

term_number = int(input("Enter term number: "))

try:
    print(f"{term_number}! = {factorial(term_number)}")
except Exception as e:
    print(e)