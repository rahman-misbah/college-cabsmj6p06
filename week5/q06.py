text = []

while True:
    line = input()
    if line == "":
        break
    text.append(line)

print("Result:")
for line in text:
    print(line.strip())
