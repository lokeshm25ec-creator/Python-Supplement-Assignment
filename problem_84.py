# Problem 84: Check if substring exists
# Fixed version

def contains_substring(text, substr):
    for i in range(len(text) - len(substr) + 1):  # fix here
        if text[i:i+len(substr)] == substr:
            return True
    return False

sentence = "Python programming is fun"
print(f"Contains 'fun': {contains_substring(sentence, 'fun')}")
