# Inverted half triangle

def inverted_triangle(n: int) -> None:
    if n <= 0: return None

    for i in range(n, 0, -1):
        print('*' * i)

height = int(input("Enter height of tower: "))
inverted_triangle(height)