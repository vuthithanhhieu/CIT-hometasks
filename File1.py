# big random value
con = 8000
# zero init list
arr = [0 for i in range(1,con+1)]
# empty res arr
res = []
# zero init counter of passed prime num
amount = 0
# first prime num init counter
i = 2;
# cicle until amount of prime num less then 1000
while amount < 1000:
    # if the number is prime
    if arr[i] == 0:
        # for each i-th number - mark it unprime
        for j in range(i+i,con,i):
            arr[j] = 1
        # that was prime - inc counter
        amount += 1
        # add prime to res
        res.append(i)
    i += 1
# print results
print(res)
# print(len(res))

'''
git init
git add file_name
git commit -m "messs"
git commit -am "messs"
git status
git --all
'''