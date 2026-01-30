# Problem 100: Calculate average of nested lists
# Fixed version

def average_nested(nested_list):
    total = 0
    count = 0

    for sublist in nested_list:
        for num in sublist:
            total += num
            count += 1

    if count == 0:        # handle empty case
        return None

    return total / count

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Average: {average_nested(data)}")

data_empty = []
print(f"Average of empty list: {average_nested(data_empty)}")