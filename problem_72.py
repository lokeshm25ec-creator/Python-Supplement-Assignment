# Problem 72: Count uppercase and lowercase letters
# Find and fix the error

def count_case(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

sentence = "Hello World"
u, l = count_case(sentence)
print(f"Uppercase: {u}, Lowercase: {l}")
