# Problem 83: Find kth smallest element
# Fixed version

def kth_smallest(arr, k):
    if k < 1 or k > len(arr):   # safety check
        return None

    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]   # fix here

numbers = [7, 10, 4, 3, 20, 15]
print(f"3rd smallest: {kth_smallest(numbers, 3)}")

