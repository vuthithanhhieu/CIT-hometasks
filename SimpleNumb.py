# beginning of prime numbers
primeNumb = 2

# counter for quantity of prime numbers
counter = 0

# list of prime numbers
primeNumbers = []

# this function determines if number is prime or not
# if prime it returns true value


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# main part
# we check if counter is less than 1000 we repeat steps over again
# until it becomes equal to 1000
# if primeNumb is prime we append it to primeNumbers list and increase counter
# and anyway increase primeNumb


while counter < 1000:
    if prime(primeNumb):
        primeNumbers.append(primeNumb)
        counter += 1
    primeNumb += 1

print(counter)
print(primeNumbers)
