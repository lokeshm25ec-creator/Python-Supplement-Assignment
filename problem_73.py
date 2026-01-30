# Problem 73: Find maximum difference between elements
# Fixed version

def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_val = arr[0]
    max_diff = arr[1] - arr[0]   # fix: real first difference

    for i in range(1, len(arr)):
        diff = arr[i] - min_val

        if diff > max_diff:
            max_diff = diff

        if arr[i] < min_val:
            min_val = arr[i]

    return max_diff

numbers = [7, 1, 5, 3, 6, 4]
print(f"Max difference: {max_difference(numbers)}")

