# Reverse string in-place
def reverse_string(string: list) -> None:
    left, right = 0, len(string) - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1

input_string = list(input("Enter a string: "))
reverse_string(input_string)
print("Reversed string:", ''.join(input_string))