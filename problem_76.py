# Problem 76: Calculate string similarity (common characters)
# Fixed version

def string_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    return len(set1 & set2)   # intersection

s1 = "hello"
s2 = "world"
print(f"Common characters: {string_similarity(s1, s2)}")

