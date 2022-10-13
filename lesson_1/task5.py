# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA = float(input('input xA: '))
yA = float(input('input yA: '))
xB = float(input('input xB: '))
yB = float(input('input yB: '))
print(round(((((xA - xB)**2) + (yA - yB)**2))**(0.5),2))



