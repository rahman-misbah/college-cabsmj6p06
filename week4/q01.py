def compute_avg(marks : list) -> float:
    return sum(marks) / len(marks)

def celsius_to_fahrenheit(celsius : float) -> float:
    return 9/5 * celsius + 32

def perimeter(length : float, breadth : float) -> float:
    return 2 * (length + breadth)

# Testing compute_avg
marks = list(map(float, input("Enter marks separated by spaces: ").split()))
print("Average Marks:", compute_avg(marks))
print()

# Testing celsius_to_fahrenheit
celsius = float(input("Enter temperature (in celsius): "))
print("Fahrenheit:", celsius_to_fahrenheit(celsius))
print()

# Testing perimeter
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
print("Perimeter:", perimeter(length, breadth))