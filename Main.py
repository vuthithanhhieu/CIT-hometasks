l=[2]
i=2
prime=False
while len(l)<1000:
    prime=True
    i=i+1
    for j in l:
        if i%j==0:
            prime=False
    if prime==True:
        l.append(i)
print(l)
print(len(l))