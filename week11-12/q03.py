data = {}

print("Enter name followed by badge number (separated by \\n). Enter 0 to end input...\n")

while True:
    name = input("Enter name: ")
    if name == "0": break
    id = int(input("Enter ID: "))
    data[name] = id

target_id = int(input("Enter ID to search for: "))

# Invert the dictionary
inverted_data = {v: k for k, v in data.items()}

if target_id in inverted_data:
    print("Owner:", inverted_data[target_id])
else:
    print("ID not found")
