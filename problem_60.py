# Improved version

def is_armstrong(n):
    if n < 0:
        return False

    num_str = str(n)
    num_digits = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    return total == n
print (f"Is 153 an Armstrong number? {is_armstrong(153)}")

print (f"Is 123 an armstrong number? {is_armstrong(123)}")


