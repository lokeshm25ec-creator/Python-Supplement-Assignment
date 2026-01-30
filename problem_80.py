# Problem 80: Find mode (most frequent element)
# Fixed version

def find_mode(lst):
    if not lst:          # handle empty list
        return None

    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1

    max_freq = max(freq.values())

    for key, value in freq.items():
        if value == max_freq:
            return key   # returns first mode

numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Mode: {find_mode(numbers)}")


