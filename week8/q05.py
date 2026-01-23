text = input("Enter a string: ")

def find_index(tokens : list, target: str) -> int:
    for idx, token in enumerate(tokens):
        if target in token:
            return idx
        
    return -1

# Tokenize
tokens = text.split()

# Normalize
tokens = map(lambda x: x.upper(), tokens)

# Sanitize
tokens = list(map(lambda x: x.replace("!", "?"), tokens))

# Find Index
target = input("Enter a substring to get its index: ").upper()
idx = find_index(tokens, target)

if idx != -1: print(f"{target} is present at {idx}")
else: print(f"{target} is not in the text")

# Find Presence
target = input("Enter a substring to know if it exists in the text: ").upper()
idx = find_index(tokens, target)

if idx != -1: print(f"{target} is in the text")
else: print(f"{target} is not in text")