
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

def display_board():
    print()
    print('| ' + board[0] + ' | ' + board[1] + ' | '  + board[2] + ' |')
    print('| ' + board[3] + ' | ' + board[4] + ' | '  + board[5] + ' |')
    print('| ' + board[6] + ' | ' + board[7] + ' | '  + board[8] + ' |')


def player1():
    print()
    player_1 = int(input(name1 +"'s " +'turn : '))
    
    if board[player_1-1] == '_':
        board[player_1 - 1] = 'X'
        print()
        display_board()
    
    else:
        print(name2 + ' has already used this block. Please select another block. ')
        player1()

def player2():
    print()
    player_2 = int(input(name2 +', its your turn : '))

    if board[player_2-1] == '_':
        board[player_2-1] = '0'
        print()
        display_board()

    else:
        print(name1 + ' has already used this block. Please select another block. ')
        player2()

def flip_players():
    global name1, name2
    print()

    name1 = input('Enter 1st players name : ')
    name2 = input('Enter 2nd players name : ')

    display_board()


    for i in range(5):
        
        player1()
        
        if board[0] == board[1] == board[2] == 'x':
            print(name1+' wins!')
            break
        elif board[3] == board[4] == board[5] == 'x':
            print('Player 1 wins!')
            break
        elif board[6] == board[7] == board[8] == 'x':
            print('Player 1 wins!')
            break
        elif board[0] == board[3] == board[6] == 'x':
            print('Player 1 wins!')
            break
        elif board[1] == board[4] == board[7] == 'x':
            print('Player 1 wins!')
            break
        elif board[2] == board[5] == board[8] == 'x':
            print('Player 1 wins!')
            break
        elif board[0] == board[4] == board[8] == 'x':
            print('Player 1 wins!')
            break
        elif board[2] == board[4] == board[6] == 'x':
            print('Player 1 wins!')
            break
        if '_' not in board:
            print()
            print('Its a tie!')
            break

        player2()

        if board[0] == board[1] == board[2] == 'y':
            print('Player 2 wins!')
            break
        elif board[3] == board[4] == board[5] == 'y':
            print('Player 2 winss!')
            break
        elif board[6] == board[7] == board[8] == 'y':
            print('Player 2 wins!')
            break
        elif board[0] == board[3] == board[6] == 'y':
            print('Player 2 wins!')
            break
        elif board[1] == board[4] == board[7] == 'y':
            print('Player 2 wins!')
            break
        elif board[2] == board[5] == board[8] == 'y':
            print('Player 2 wins!')
            break
        elif board[0] == board[4] == board[8] == 'y':
            print('Player 2 wins!')
            break
        elif board[2] == board[4] == board[6] == 'y':
            print('Player 2 wins!')
            break
        if '_' not in board:
            print()
            print('Its a tie!')
            break








   

flip_players()

#player1()
#player2()









