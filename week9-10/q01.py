# Find maximum and minimum

closing_prices = list(map(float, input("Enter closing prices (separated by space): ").split()))
print("Peak:", max(closing_prices))
print("Trough:", min(closing_prices))