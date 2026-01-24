def frequency_counter(text: str) -> dict:
    counter = {}

    for i in text:
        if i in counter: counter[i] += 1
        else: counter[i] = 1
    
    return counter

text = input("Enter a string: ")
frequency = frequency_counter(text)

print(frequency)    