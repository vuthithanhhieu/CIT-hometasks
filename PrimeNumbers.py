import math

count = 1000
array = [i for i in range(2, int(math.sqrt(count)) + 1)]
for i in range(2, int(math.sqrt(count)) + 1):
    for j in list(array):
        if j % i == 0 and j != i:
            array.remove(j)

last = array[-1] + 1
while True:
    if len(array) >= count:
        break
    array.append(last)
    for i in array[0:-1]:
        if array[-1] % i == 0:
            array.pop()
            break
    last += 1

print(array)
