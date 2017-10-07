import math

a = [i for i in range(2, 10000)]

for i in range(0, int(math.sqrt(len(a) - 1))):
    for j in range(i + 1, len(a)):
        if a[i] != 0 and a[j] % a[i] == 0:
            a[j] = 0

a = [i for i in a if i != 0][:1000]
print(a)
