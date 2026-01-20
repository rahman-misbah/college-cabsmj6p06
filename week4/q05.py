def digit_sum(num : int) -> int:
    result = 0

    while num > 0:
        result += num % 10
        num //= 10
    
    return result

num = int(input("Enter a number: "))
print("Digit Sum:", digit_sum(num))
