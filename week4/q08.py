def count_upper_lower_cases(string : str) -> tuple:
    upper_case = 0
    lower_case = 0
    
    for i in string:
        if not i.isalpha(): continue
        if i.isupper(): upper_case += 1
        else: lower_case += 1
    
    return lower_case, upper_case

string = input("Enter a string: ")
lower_case, upper_case = count_upper_lower_cases(string)
print(f"Lower case letters: {lower_case}")
print(f"Upper case letters: {upper_case}")