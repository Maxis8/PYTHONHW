# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# степень
def pow_eq(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num
# коэффицент
def k_eq(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def sort_eq(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if pow_eq(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    index = l-1 
    while index >= 0:
        if pow_eq(st[index]) != -1 and pow_eq(st[index]) == i:
            lst.append(k_eq(st[index]))
            index -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    
# создание  файлов
s1 = '2x^4 + 23x^3 + 11x^2 + 5x + 9 = 0'
s2 = '27x^5 + 10x^4 + 7x^3 + 11x^2 + 33x + 3 = 0'
with open("equation_1.txt", 'w') as data:
    data.write(s1)
with open("equation_2.txt", 'w') as data:
    data.write(s2)

#  сумма многочлена
with open('equation_1.txt', 'r') as data:
    st1 = data.readlines()
with open('equation_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = sort_eq(st1)
lst2 = sort_eq(st2)
ln = len(lst1)
if len(lst1) > len(lst2):
    ln = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ln)]
if len(lst1) > len(lst2):
    s = len(lst1)
    for i in range(ln,s):
        lst_new.append(lst1[i])
else:
    s = len(lst2)
    for i in range(ln,s):
        lst_new.append(lst2[i])
# создание строки
lst= lst_new[::-1]
wr = ''
if len(lst) < 1:
        wr = 'x = 0'
else:
 for i in range(len(lst)):
    if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
        wr += f'{lst[i]}x^{len(lst)-i-1}'
        wr += ' + '
    elif i == len(lst) - 2 and lst[i] != 0:
        wr += f'{lst[i]}x'
        if lst[i+1] != 0:
            wr += ' + '
    elif i == len(lst) - 1 and lst[i] != 0:
        wr += f'{lst[i]} = 0'
    elif i == len(lst) - 1 and lst[i] == 0:
        wr += ' = 0'
with open("equation_res.txt", 'w')as data:
    data.write(wr)
with open('equation_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результат {st3}")

