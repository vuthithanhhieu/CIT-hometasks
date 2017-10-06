import math

N = 1000
count = 0

first = 0
last = 10
array = [i for i in range(first + 2, last + 1)]
while count < N:
    for i in range(0, int(math.sqrt(last))):
        for j in range(i + 1, len(array)):
            if array[i] != 0 and array[j] % array[i] == 0:
                array[j] = 0
    array = [i for i in array if i != 0]
    count = len(array)
    if count < N:
        first = last + 1
        last = last * 2
        temp = [i for i in range(first, last)]
        array.extend(temp)
    else:
        array = [i for i in array[0:N]]
        break

print(array)
