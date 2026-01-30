def remove_adjacent_duplicates(text):
    result = []
    for c in text:
        if not result or result[-1] != c:
            result.append(c)
    return "".join(result)

