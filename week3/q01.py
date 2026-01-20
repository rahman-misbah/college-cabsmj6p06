values = list(map(int, input("Enter values separated by space: ").split()))

value_sum = sum(values)
value_product = 1

for value in values:
    value_product *= value

value_avg = value_sum / len(values) if values else 0

print(f"Sum: {value_sum}")
print(f"Product: {value_product}")
print(f"Average: {value_avg}")