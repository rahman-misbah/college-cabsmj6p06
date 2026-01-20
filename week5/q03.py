# Text Filter
def filter_text(text):
    curr_index = 0
    result = []

    for char in text:
        if not char.isalpha(): continue
        if curr_index % 2 == 0: 
            curr_index += 1
            continue
        
        result.append(char)
        curr_index += 1
    
    return ''.join(result)

text = input("Enter text: ")
print("Filtered text:", filter_text(text))