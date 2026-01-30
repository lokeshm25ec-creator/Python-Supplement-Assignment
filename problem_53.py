# Problem 53: Check if two strings are anagrams
# Fixed version

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

word1 = "Listen"
word2 = "Silent"
print(f"Are anagrams: {are_anagrams(word1, word2)}")

