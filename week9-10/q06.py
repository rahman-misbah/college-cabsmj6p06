def bubble_sort(sequence: list) -> None:
    last_idx = len(sequence) - 1
    swapped = None

    for i in range(last_idx, -1, -1):
        swapped = False

        for j in range(i):
            if sequence[j] > sequence[j+1]:
                swapped = True
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
        
        if not swapped: break

sequence = list(map(int, input("Enter numbers separated by space: ").split()))
bubble_sort(sequence)

print("Sorted List:", sequence)