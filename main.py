def isprime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

print ([x for x in range(2, 10000) if isprime(x)])
