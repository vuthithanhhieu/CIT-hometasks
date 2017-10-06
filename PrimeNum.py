def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Введите номер простого числа: "))
count = 0
x=0

while count <= number:
    x+=1
    if prime(x):
        count+=1

print('Простое число под номером',number,'равно',x)
