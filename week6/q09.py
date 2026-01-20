# Verify consecutive integers
def are_consecutive_integers(lst):
    if not lst:
        return False
    
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] + 1 != sorted_lst[i + 1]:
            return False
    return True

input_list = list(map(int, input("Enter integers separated by spaces: ").split()))

if are_consecutive_integers(input_list):
    print("The list contains valid level IDs.")
else:
    print("The list does not contain valid levle IDs.")