import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = 'X'
winner = None
game_running = True


# print board

def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# take input

def player_input(board):
    inp = int(input('Enter a num between 1-9: '))
    if inp >= 1 and inp <=9 and board[inp-1] == '-':
        board[inp-1] = current_player
    else:
        print('Invalid Input')


# check for win or tie

def check_row(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def check_column(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    
def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

# check for tie

def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print('its a tie')
        game_running = False


# check for win

def check_win():
    global game_running
    if check_column(board) or check_row(board) or check_diag(board):
        print_board(board)
        print(f'winner is {winner}')
        game_running = False


# switch players

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# check for win or tie again

# computer

def computer(board):
    while current_player == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = 'O'
            switch_player()

while game_running:
    print_board(board)
    player_input(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
