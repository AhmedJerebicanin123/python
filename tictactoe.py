import random

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

currentPlayer = 'X'
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8]) 

def playerinput(board):
    inp = int(input('Unesite broj od 1 do 9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Igrac je vec na toj poziciji')

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0] 
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkrow(board):
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

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0] 
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2] 
        return True
  
def checktie(board):
    if '-' not in board:
        printBoard(board)
        print('Nereseno je')
        gameRunning = False

def computer(board):
    while currentPlayer == 'O':
     position = random.randint(0, 8)
     if board[position] == '-':
            board[position] = 'O'
            switchplayer()

def switchplayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
        
def checkwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f'Pobednik je {winner}')
        gameRunning = False
        quit()

while gameRunning:
    printBoard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
