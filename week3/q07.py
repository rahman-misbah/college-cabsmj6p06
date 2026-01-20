# Multiply by 10 using bitwise operations

score = int(input("Enter an integer score: "))
score = (score << 3) + (score << 1)

print("Score multiplied by 10 is:", score)