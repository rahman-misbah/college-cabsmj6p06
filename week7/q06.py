# Split list into lists of evens and odds
def id_filter(id_list: list) -> tuple[list, list]:
    low_priority = [] # even numbers
    high_priority = [] # odd numbers

    for id in id_list:
        if id % 2 == 0: low_priority.append(id)
        else: high_priority.append(id)
    
    return low_priority, high_priority

id_list = list(map(int, input("Enter IDs separated by space: ").split()))
low, high = id_filter(id_list)

print("Low Priority IDs:", low)
print("High Priority IDs:", high)