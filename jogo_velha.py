token = ['X', 'O']
def criarBoard():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board


def printBoard(board):
    for i in range(3):
        print('|'.join(board[i]))
        if i < 2:
            print('-----')


def getInputValido(msg):
    try:
        n = int(input(msg))
        if n >=1 and n <=3:
            return n
        else:
            print('O número precisa estar entre 1 e 3')
            return getInputValido(msg)
    except:
        print('Número inválido')
        return getInputValido(msg)



def verificarMovimento(i, j, board):
    if(board[i-1][j-1] == ' '):
        return True
    else:
        return False


def fazerMovimento(i, j, board, jogador):
    board[i-1][j-1] = token[jogador]

def verificarGanhador(board):
    #linha
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' '):
            return board[i][0]

    #coluna
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' '):
            return board[0][i]

    #diagonal principal
    if(board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    if (board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return 'EMPATE'