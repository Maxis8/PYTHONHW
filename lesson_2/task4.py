# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .
from random import randint
lst = [randint(-44,77) for i in range(10)]
num1 = int(input("Введите число1: "))
num2 = int(input("Введите число2: "))
mult = lst[num1]* lst[num2]
print(f'{lst}  {lst[num1]} * {lst[num2]} = {mult}')

