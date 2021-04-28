from jogo_velha import printBoard, verificarGanhador, verificarMovimento, fazerMovimento, criarBoard, getInputValido

jogador = 0 #jogador 1
board = criarBoard()
ganhador = verificarGanhador(board)

while(not ganhador):
    printBoard(board)
    i = getInputValido('Digite a linha: ')
    j = getInputValido('Digite a coluna: ')

    if(verificarMovimento(i, j, board)):
        fazerMovimento(i, j, board, jogador)
        jogador = (jogador + 1)%2
    else:
        print('A posição informada já está ocupada')

    ganhador = verificarGanhador(board)

print("======================================")
printBoard(board)
print('GANHADOR: {}'.format(ganhador))