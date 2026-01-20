# Word frequency counter
def clean_word(word: str) -> str:
    cleaned_word = ''

    for char in word:
        if char.isalnum():
            cleaned_word += char.lower()
    
    return cleaned_word

def word_frequency_counter(text):
    # Remove punctuation and convert to lowercase
    text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    frequency = {}
    for word in words:
        word = clean_word(word)

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

text = input("Enter text: ")

frequency = word_frequency_counter(text)

for word, count in frequency.items():
    print(f"{word}: {count}")
