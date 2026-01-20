# Count occurrence of ints
def count_ints(sequence: list) -> int:
    count = 0

    for item in sequence:
        if isinstance(item, int):
            count += 1
    
    return count

sequence = [1, 'two', 3, 4.0, 5, 'six', 7]
result = count_ints(sequence)
print(f"Number of integers in the sequence: {result}")