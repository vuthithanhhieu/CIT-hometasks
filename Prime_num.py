n = 100000
a = range(n + 1)
a[1] = 0
lst = []

i = 2
while i <= 10000:
    if a[i] != 0:
        lst.append(a[i])
        for j in xrange(i, n + 1, i):
            a[j] = 0
    i += 1

    if len(lst) > 999:
        break
print (lst)