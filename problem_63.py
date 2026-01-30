def find_longest_word(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

