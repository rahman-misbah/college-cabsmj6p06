# Vowel and Consonant Counter

def count_vowels(string: str) -> int:
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in string:
        if char in vowels:
            print(char, end=" ")
            vowel_count += 1
    print()

    return vowel_count

def count_consonants(string: str) -> int:
    
    vowels = "aeiouAEIOU"
    consonant_count = 0
    
    for char in string:
        if char.isalpha() and char not in vowels:
            print(char, end=" ")
            consonant_count += 1
    print()

    return consonant_count

string = input("Enter a string: ")

print()
print(f"{'#'*10}Vowels{'#'*10}")
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)

print()
print(f"{'#'*10}Consonants{'#'*10}")
consonant_count = count_consonants(string)
print("Number of consonants:", consonant_count)