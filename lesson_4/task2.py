# 2.Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
num = int(input('Введите число: '))
mults = []
i = 2
while num != 1:
    
    if num % i == 0:
     mults.append(i) 
     num = num // i
     
    elif  (num % i+1) == 0:
        mults.append(i)
        num = num // i
    else:
        i+=1    
print(*mults, sep = ' x ')     