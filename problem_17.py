# Problem 17: Capitalize first letter of each word
# Find and fix the error

def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())

sentence = "hello world from python"
print(capitalize_words(sentence))
