# SKU generator
def sku_of(product_name: str) -> str:
    if len(product_name) < 2: return ""
    return product_name[:2] + product_name[-2:]

product = input("Enter product name: ")
print("SKU Code:", sku_of(product))