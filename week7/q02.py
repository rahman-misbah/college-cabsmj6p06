# Fibonacci (recursive)
def fibonacci(n: int, cache: dict = {1: 0, 2: 1}):
    if n <= 0:
        return -1
    if n in cache: return cache[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result

    return result

term = int(input("Enter term number(n): "))

if term <= 0:
    print("Term must be a positive number")
else:
    for i in range(1, term + 1):
        print(fibonacci(i), end=" ")
    print()
