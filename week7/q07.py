# Palindrome checker
def is_palindrome(n: int) -> bool:
    if n < 0 or (n % 10 == 0 and n != 0): return False
    
    n_str = str(n)

    return n_str == n_str[::-1]

num = int(input("Enter an integer: "))

if is_palindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")