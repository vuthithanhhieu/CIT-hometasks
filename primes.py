import math
n=10000
print("primes with loops")
primes=list(range(n+1))
primes[0]=primes[1]=0

for i in range(2,int(math.sqrt(n))):
    for j in range(i+i,n+1,i):
        primes[j]=0
primes=[primes for primes in primes if primes!=0]
print(primes[0:1000])

print("primes with generators")
#need wait...
primesline=[prime for prime in range(2,n+1) if prime not in [pr for j in [list(range(i+i,n+1,i)) for i in range(2,int(math.sqrt(n)))] for pr in j]]
print(primesline[0:1000])