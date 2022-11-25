
def import_data(data, sep):
    with open('phone.csv','phone.txt', 'a+', encoding = 'utf-8') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        
        else:
            file.write(sep.join(data))
            file.write(f"\n")
            








def export_data():
    with open('phone.csv', 'r', encoding = 'utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
        data =[j for i in data for j in i]            
    return data

def export_datas():
    with open('phone.csv', 'r', encoding = 'utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t =[]
    return data               


def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None    
    
def choice_sep():
        sep = input("Введите разделитель: ")
        if sep == " ":
            sep = None
        else:
            sep = None
        return sep         