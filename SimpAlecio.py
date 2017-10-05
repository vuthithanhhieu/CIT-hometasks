par=1000
arr=[]
arr.append(2)
arr.append(3)
counter=4
while len(arr)<par:
    if counter%2!=0 and counter%3!=0:
        temp=4
        while temp*temp<=counter:
            if counter%temp==0:
                break
            temp += 1
        if temp*temp>counter:
            arr.append(counter)
    counter +=1
print(arr)
