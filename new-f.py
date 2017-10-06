n = 0
m = 100000
k = 0

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0 : d += 2
    return d * d > n

while k <= m:
    n+=1
    if isPrime(n) == 1:
        k+=1

print(n)