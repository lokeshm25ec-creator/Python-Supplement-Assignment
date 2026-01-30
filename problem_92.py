def all_unique(lst):
    seen = []
    for item in lst:
        if item in seen:
            return False
        seen.append(item)
    return True

