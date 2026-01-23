# Check for existence

product_ids = list(map(int, input("Enter product IDs (separated by space): ").split()))
target = int(input("Enter ID to search: "))

if target in product_ids:
    print("Found")
else:
    print("Not Found")