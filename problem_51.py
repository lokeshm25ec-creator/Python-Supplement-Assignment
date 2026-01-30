# Problem 51: Reverse words in a sentence
# Fixed version

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")

