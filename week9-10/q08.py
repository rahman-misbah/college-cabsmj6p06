import random

# Quick Sort

def quick_sort(arr: list, low: int = None, high: int = None):
    if low is None or high is None:
        low = 0
        high = len(arr) - 1
    
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr: list, low: int, high: int):      # Uses random pivots
    # Randomize pivot
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]

    # Basic partition logic
    pivot_key = arr[low]
    i, j = low + 1, high

    while i <= j:
        while i <= j and arr[i] <= pivot_key:
            i += 1
        while j >= i and arr[j] >= pivot_key:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[low] = arr[low], arr[j]

    return j

lst = list(map(int, input("Enter numbers separated by space: ").split()))
quick_sort(lst)

print("Sorted Array:", lst)