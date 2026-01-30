# Problem 57: Find LCM of two numbers
# Find and fix the error

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
def gcd(a, b):
    while b:
        a, b = b, a % b
        return a
