# Problem 90: Find median of a list
# Fixed version

def find_median(lst):
    if not lst:          # handle empty list
        return None

    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 0:
        median = (sorted_lst[n//2] + sorted_lst[n//2 - 1]) / 2
    else:
        median = sorted_lst[n//2]

    return median

numbers = [1, 3, 5, 7, 9]
print(f"Median: {find_median(numbers)}")

empty_list = []
print(f"Median of empty list: {find_median(empty_list)}")