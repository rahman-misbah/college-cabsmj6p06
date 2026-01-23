# Sort filename based on character length

files = []
name = None

print("Write 0 to end input...\n")

while name != "0":
    name = input("Enter a filename: ")
    
    if name != "0": files.append(name)

files.sort(key=lambda x: len(x))

print("Sorted files:", files)