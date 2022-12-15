import logging

logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="a",encoding = 'utf-8',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")




def sort_data(choice,read,write,sor,sor1,da,data):
    while True: 
        d=choice()
        if d=='1':
            print(*da(0,read()),sep='\n')    
            logging.debug("Вывод фамилий всех учеников" +  str(da(0,read())))
        elif d=='2':
            logging.debug("Вывод имён всех учеников" +  str(da(1,read())))
            print(*da(1,read()),sep='\n')        
        elif d=='3':
            print(*da(2,read()),sep='\n')    
        elif d=='4':
            print(*sor(input('Введите № класса: '),read()),sep='')   
        elif d=='5':
            print(*read(),sep='')
            logging.info("Вывод всей таблицы" +  str(read()))
        elif d=='6':
            print(*sor(input('Введите фамилию ученика:'),read()),sep='')    
            logging.debug("Вывод данных об ученике " )
        elif d=='7':
            logging.debug("Данные ученика "  + str(data()))
            write(data())
        elif d=='8':
            print(*sor1(input('Введите оценку: '),read()),sep='')
        elif d=='9':
            logging.debug("Выход из программы")
            print('See you!')        
            break



