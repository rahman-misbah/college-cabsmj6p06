# GCD (recursion)
# Two layer pattern ensures that a and b are checked only
# once, instead of being checked each cycle
def find_signal_sync(a: int, b: int) -> int: 
    if a < 0 or b < 0: return -1

    def _gcd(a: int, b: int) -> int:
        if b == 0: return a
        return _gcd(b, a % b)

    return _gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = find_signal_sync(a, b)

if result == -1:
    print("Numbers must be non-negative!")
else:
    print("Result:", result)
    