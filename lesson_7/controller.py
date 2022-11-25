import data_actions
import enter_info
import view 

    
   
    
    

def start():
    print("Выберите действие:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = data_actions.choice_sep()
        data_actions.import_data(enter_info.get_data(), sep)
    elif ch == '2':
        data = data_actions.export_data()
        view.print_data(data)
        
    else:
        word = input("Введите данные для поиска: ")
        data = data_actions.export_datas()
        item = data_actions.search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20),  "Телефон".center(15), "Описание".center(30))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20))
        else:
            print("Данные не обнаружены")
            return start
        
        