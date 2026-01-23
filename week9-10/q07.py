# Merge Sort

def merge_sort(arr: list, low: int = None, high: int = None) -> None:
    if low is None or high is None:
        low = 0
        high = len(arr) - 1

    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, high)

def merge(arr: list, low: int, high: int) -> None:
    mid = (low + high ) // 2
    merged_arr = []
    i, j = low, mid + 1     # i tracks left half, j tracks right half

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            merged_arr.append(arr[i])
            i += 1
        else:
            merged_arr.append(arr[j])
            j += 1
    
    # Append remaining items
    while i <= mid:
        merged_arr.append(arr[i])
        i += 1
    
    while j <= high:
        merged_arr.append(arr[j])
        j += 1
    
    # Place sorted section in original list
    for idx in range(high, low - 1, -1):
        arr[idx] = merged_arr.pop()

lst = list(map(int, input("Enter numbers separated by space: ").split()))
merge_sort(lst)

print("Sorted Array:", lst)