from collections import Counter

def first_non_repeating(text):
    count = Counter(text)

    for char in text:
        if count[char] == 1:
            return char
    return None

