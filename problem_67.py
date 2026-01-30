# Problem 67: Remove nth element from list
# Fixed version

def remove_nth(lst, n):
    if -len(lst) <= n < len(lst):   # allow negative index
        return lst[:n] + lst[n+1:]
    return lst

numbers = [1, 2, 3, 4, 5]
result = remove_nth(numbers, 2)
print(f"After removing: {result}")

