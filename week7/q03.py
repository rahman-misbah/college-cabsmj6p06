# Factorial (recursive)
def create_factorial_fxn():
    cache = {0 : 1}

    def factorial(n: int) -> int:
        if n < 0: return -1
        if n in cache: return cache[n]

        result = n * factorial(n - 1)

        cache[n] = result

        return result
    
    return factorial

factorial = create_factorial_fxn()

num = int(input("Enter a number to get its factorial: "))
print(f"{num}! = {factorial(num)}")