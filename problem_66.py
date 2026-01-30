# Problem 66: Find intersection of two lists
# Fixed version

def intersection(list1, list2):
    set2 = set(list2)
    result = []

    for item in list1:
        if item in set2 and item not in result:
            result.append(item)

    return result

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print(f"Intersection: {intersection(l1, l2)}")

