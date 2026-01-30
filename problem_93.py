def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for word in strs:
            if word[i] != ch:
                return shortest[:i]

    return shortest

