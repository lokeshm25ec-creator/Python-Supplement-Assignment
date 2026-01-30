# Problem 21: Check if list is sorted
# Find and fix the error

def is_sorted(lst):
    return lst == sorted(lst)

numbers = [1, 2, 3, 4, 5]
print(f"Is sorted: {is_sorted(numbers)}")
