# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


lst = [3,4,7,6,2,5,7]
mult = []
length = len(lst)
for i in range(len(lst)):
    while i < len(lst)/2 and length > len(lst)/2:
        length = length - 1
        a = lst[i] * lst[length]
        mult.append(a)
        i += 1

print(lst)
print(mult)


