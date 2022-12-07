def get_da(j,t):
    li=[]
    for i in t:
        li.append(i.split()[j])
    return li


def sort(j,t):
    li=[]
    for i in t:
        if j in i:
            li.append(i)
    return li    

def sort1(j,t):
    li=[]
    for i in t:
        if j in i:
            li.append(i.split()[0]+' ')
            li.append(i.split()[1]+' ')
            li.append(i.split()[3]+'\n')
    return li    