# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
n = int(input('Введите число: '))
num = n
res = []
while num > 0:
    if num % 2 == 0:
     res.insert(0,0)
     num =int(num / 2)
    else:
     res.insert(0,1)
     num =int(num / 2)
print(n, ' -> ', *res, sep ='' )
    