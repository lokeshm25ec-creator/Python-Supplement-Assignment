# Problem 89: Check if number is palindrome
# Fixed version

def is_palindrome_number(n):
    if n < 0:
        return False   # negative numbers are not palindromes

    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return original == reversed_num

print(f"Is 121 palindrome? {is_palindrome_number(121)}")

