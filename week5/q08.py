# Reverse words while keeping words in order
def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

sentence = input("Enter a sentence: ")
result = reverse_words(sentence)
print("Reversed words:", result)