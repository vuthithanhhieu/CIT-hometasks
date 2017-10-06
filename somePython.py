primes = [2] 
s = 3
while len(primes) < 1000:
    flag = 0;
    for item in primes: 
        if s%item == 0: 
            flag=1
            break 
    if not flag:
        primes.append(s) 
    s +=1 
print(primes) 
print(len(primes))
