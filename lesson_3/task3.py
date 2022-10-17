# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2,  3.1, 5, 10.01, 7, 11.35]
new = []
for i in lst:
    num = i - int(i)
    num = round((num),2)
    new.append(num)
max = new[0]
min = new[0]
for i in range(1,len(new)):
    if new[i] ==0 :
        continue
    if new[i] > max:
        max = new[i]
    elif  new[i] < min:
        min = new[i]
res =round((max - min),2)        
print(f'{lst} => {res}')



  


   