def fibonacci():
    curr_term = 0
    next_term = 1

    while True:
        yield curr_term
        curr_term, next_term = next_term, curr_term + next_term

# Verify fibonacci sequence
fib = fibonacci()

user_in = list(map(int, input("Enter fibonacci sequence separated by spaces: ").split()))

for num in user_in:
    if num != next(fib):
        print("Incorrect fibonacci sequence.")
        break
else:
    print("Correct fibonacci sequence.")