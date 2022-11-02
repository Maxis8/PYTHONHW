# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random

k =  int(input('Введите число: '))
lst= [random.randint(-100,101)for i in range(k+1)]
st = ''
for i in range(len(lst)):
            
            if lst[i] != 0 and  i != len(lst) - 1  and i != len(lst) - 2:
                st += f'{lst[i]}x^{len(lst)-i-1}'
                st += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                st += f'{lst[i]}x'
                if lst[i+1] != 0:
                 st += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                st += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                st += ' = 0'

with open('equation.txt', 'w') as data:
         data.write(st)
print(st)







