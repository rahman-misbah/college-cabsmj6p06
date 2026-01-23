# Verbose InsertionSort

def insertion_sort(sequence: list, verbose: bool = False) -> None:
    if verbose: print(sequence)

    for key_idx in range(1, len(sequence)):
        key = sequence[key_idx]
        curr_idx = key_idx - 1
        
        while curr_idx >= 0 and sequence[curr_idx] > key:
            sequence[curr_idx + 1] = sequence[curr_idx]
            curr_idx -= 1

        sequence[curr_idx + 1] = key

        if verbose: print(sequence)

lst = list(map(int, input("Enter numbers separated by space: ").split()))
insertion_sort(lst, True)
print("Final Result", lst)