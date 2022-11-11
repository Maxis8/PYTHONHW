# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint
fin = ''
while fin !='no':
    candies = int(input('Enter digit: '))
    flag = randint(0,1)
    if flag:
        print('User ')
    else:
        print('AI') 
      
    while candies > 28:
            if flag : 
                u1 = int(input('User: ' )) 
                while u1 > 28 or u1 <1:
                    u1 = int(input('Enter no more then 28 at least 1: '))
                candies-=u1
                print(f'{candies} left\n') 
                flag = False
            else:        
                u2 = randint(1,28)
                print(f'AI:{u2}')
                candies-=u2
                print(f'{candies} left\n')          
                flag =True
    if flag: 
        print('User win') 
    else:
        print('AI win')                
    fin = input('continue? yes or no:')
            