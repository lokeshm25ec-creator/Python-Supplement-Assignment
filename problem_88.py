# Problem 88: Find all substrings of a string
# Fixed version

def all_substrings(text):
    substrings = []

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):   # fix here
            substrings.append(text[i:j])

    return substrings

word = "abc"
print(f"All substrings: {all_substrings(word)}")
