# Problem 65: Check if list has duplicates
# Fixed version

def has_duplicates(lst):
    seen = set()   # use set

    for item in lst:
        if item in seen:
            return True
        seen.add(item)

    return False

numbers = [1, 2, 3, 4, 5]
print(f"Has duplicates: {has_duplicates(numbers)}")

