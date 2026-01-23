election_tally = dict()

print("Enter Names and votes (separated by space). Enter 0 to end input...\n")

while True:
    user_in = input("Name and votes: ")

    if user_in == "0": break

    user_in = user_in.split()
    election_tally[user_in[0]] = int(user_in[1])
print()

sorted_tally = list(election_tally.items())
sorted_tally.sort(key=lambda x: x[1])

if sorted_tally:
    print("Winner:", sorted_tally[-1][0])
    print("Least Votes:", sorted_tally[0][0])
else:
    print("No input detected!")