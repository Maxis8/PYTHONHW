# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def ChekNum(numb):
 while(int(numb) == numb):
    numb = float(input('Введите вещественное число: '))
 return numb

def SumNum(num):
  num = str(num).split('.')
  num = (num[0] + num[1])
  num = int(num)
  sum = 0
  while(num>0):
    sum += num % 10
    num = (num // 10)
  return sum

number = float(input('Введите вещественное число: '))
print(SumNum(ChekNum(number)))










