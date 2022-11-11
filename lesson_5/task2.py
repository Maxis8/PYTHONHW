# Создайте программу для игры в ""Крестики-нолики"".


print('Start!')

board = list(range(1,10))

def desk(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Ещё')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'X0'):
                board[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз ')

def check_win(board):
    win = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    count =0
    victory = False
    while not victory:
        desk(board)
        if count % 2 == 0:
            choice('X')
        else:
            choice('0')
        count +=1
        if count > 4:
            win_tab = check_win(board)
            if win_tab:
                print(win_tab,'Победа')
                victory = True
                break
            if count == 9:
                print('Ничья)')
        desk(board)
game(board)