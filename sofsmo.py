def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
def primes(n = 1):
    while(True):
        if isprime(n): yield(n)
        n += 1
c=0
for n in primes():
    c+=1
    print(n)
    if c > 1000: break