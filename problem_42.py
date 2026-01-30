words = ["Hello", "World", "Python"]
sentence = ""

for word in words:
    sentence += word + " "

sentence = sentence.strip()   # remove extra space
print(f"Sentence: {sentence}")

