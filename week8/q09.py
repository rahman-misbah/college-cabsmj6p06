# Binary Search

def binary_search(sequence, target, key = None):
    start = 0
    end = len(sequence) - 1
    if key is None: key = lambda x: x

    while start <= end:
        mid = (start + end) // 2

        if key(sequence[mid]) == target: return mid
        
        if key(sequence[mid]) > target: end = mid - 1
        else: start = mid + 1

    return -1

book_id = list(map(int, input("Enter Book IDs separated by space: ").split()))
target = int(input("Enter ID to search: "))

book_id = [(id, idx) for idx, id in enumerate(book_id)]
book_id.sort(key=lambda x: x[0])

target_idx = binary_search(book_id, target, key=lambda x: x[0])

if target_idx == -1: print(f"Book ID {target} not in catalog")
else: print(f"Book ID {target} at index {book_id[target_idx][1]}")