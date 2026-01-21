def bubble_sort(sequence: list) -> None:
    last_idx = len(sequence) - 1

    for i in range(last_idx, -1, -1):
        for j in range(i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

sequence = list(map(int, input("Enter numbers separated by space: ").split()))
bubble_sort(sequence)

if len(sequence) > 1:
    print("Second largest element:", sequence[-2])
else:
    print("List must have at least 2 elements")