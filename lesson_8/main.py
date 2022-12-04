def sort_data(choice,read,write,sor,sor1,da,data):
    while True: 
        d=choice()
        if d=='1':
            print(*da(0,read()),sep='\n')    
        elif d=='2':
            print(*da(1,read()),sep='\n')        
        elif d=='3':
            print(*da(2,read()),sep='\n')    
        elif d=='4':
            print(*sor(input('Введите № класса: '),read()),sep='')   
        elif d=='5':
            print(*read(),sep='')
        elif d=='6':
            print(*sor(input('Введите фамилию ученика:'),read()),sep='')    
        elif d=='7':
            write(data())
        elif d=='8':
            print(*sor1(input('Введите оценку: '),read()),sep='')
        elif d=='9':
            print('See you!')        
            break