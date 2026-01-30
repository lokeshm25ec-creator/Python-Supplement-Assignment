# Problem 70: Find all prime numbers up to n
# Fixed version

def find_primes(n):
    primes = []

    for num in range(2, n + 1):   # include n
        is_prime = True

        for i in range(2, int(num**0.5) + 1):   # check till sqrt
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

print(f"Primes up to 20: {find_primes(20)}")

