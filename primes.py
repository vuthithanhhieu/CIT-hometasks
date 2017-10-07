import math

n = 1000
boolPrimes = [True for l in range(0, 10 * n - 1)]
for i in range(0, int(math.sqrt(10 * n) - 1)):
    if boolPrimes[i] is True:
        for j in range(i + i + 2, 10 * n - 1, i + 2):
            if boolPrimes[j] is True:
                boolPrimes[j] = False
primes = [p + 2 for p in range(0, 10 * n - 1) if boolPrimes[p]][:n]
print(primes)