import random
computerSign = 'X'
playerSign = 'O'

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard(board):
    for width in range(3):
        # for height in range(3):
        if width == 0:
            print(3 * '|=========|')
        print(3 * '|         |')
        for k in range(3):
            print('|    ' + str(board[k + width * 3]) + '    |', end="")
        print("")
        print(3 * '|         |')
        print(3 * '|=========|')


def enterMove(board):
    while True:
        try:
            move = int(input("Podaj liczbę:"))
            if move in makeListOfFreeFields(board) and move > 0 and move < 10:
                return move - 1
            else:
                continue
        except ValueError:
            print("Wprowadź liczbę od 1 do 9")
        except:
            print("Błąd")

def computerMove(board, counter):
    if counter == 0:
        counter += 1
        return 4
    else:
        while True:
            move = random.randrange(1, 10, 1)
            if move in makeListOfFreeFields(board):
                return move - 1


def makeListOfFreeFields(board):
    list = []
    for i in board:
        if i != playerSign and i != computerSign:
            list.append(i)
    return list


def isVictory(board):
    for i in range(3):
        # poziom
        if (board[3 * i] == board[3 * i + 1]) and (board[3 * i] == board[3 * i + 2]):
            return [3 * i, 3 * i + 1, 3 * i + 2]
        # pion
        elif (board[i] == board[i + 3]) and (board[i] == board[i + 6]):
            return [i, i + 3, i + 6]
    # ukos \
    if board[0] == board[4] and board[0] == board[8]:
        return [0, 4, 8]
    # ukos /
    elif board[2] == board[4] and board[2] == board[6]:
        return [2, 4, 6]
    elif len(makeListOfFreeFields(board)) == 0:
        return []


def skreslZwyciezce(doSprawdzenia, board):
    pomocninicza = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(3):
        # poziom
        if doSprawdzenia[0] == pomocninicza[3 * i] and doSprawdzenia[1] == pomocninicza[3 * i + 1] and doSprawdzenia[
            2] == pomocninicza[3 * i + 2]:
            board[3 * i] = board[3 * i + 1] = board[3 * i + 2] = '-'
            return
        # pion
        elif doSprawdzenia[0] == pomocninicza[i] and doSprawdzenia[1] == pomocninicza[i + 3] and doSprawdzenia[2] == \
                pomocninicza[i + 6]:
            board[i] = board[i + 3] = board[i + 6] = '|'
            return

        #   skos \
    if doSprawdzenia[0] == pomocninicza[0] and doSprawdzenia[1] == pomocninicza[4] and doSprawdzenia[2] == pomocninicza[
        8]:
        board[0] = board[4] = board[8] = '\\'
        return
        #     skos /
    elif doSprawdzenia[0] == pomocninicza[2] and doSprawdzenia[1] == pomocninicza[4] and doSprawdzenia[2] == \
            pomocninicza[6]:
        board[2] = board[4] = board[6] = '/'
        return


def isEnd(board):
    x = isVictory(board)
    if x == None:
        return False
    else:
        if len(makeListOfFreeFields(board)) == 0 and len(x) == 0:
            printBoard(board)
            print("REMIS")
            return True
        elif board[x[0]] == computerSign:
            skreslZwyciezce(x, board)
            printBoard(board)
            print("KOMPUTER WYGRYWA")
            return True
        elif board[x[0]] == playerSign:
            skreslZwyciezce(x, board)
            printBoard(board)
            print("GRACZ WYGRYWA")
            return True

def computerLogicDefence(board):
    for i in range(3):
        # poziom
        if board[3 * i] == board[3 * i + 1] and board[3*i]==playerSign and board[3 * i + 2] != computerSign:
            return 3 * i + 2
        elif board[3 * i + 2] == board[3 * i + 1]  and board[3*i+1]==playerSign and board[3 * i] != computerSign:
            return 3 * i
        elif board[3 * i] == board[3 * i + 2]  and board[3*i]==playerSign and board[3 * i + 1] != computerSign:
            return 3 * i + 1
        # pion
        if board[i + 3] == board[i] and board[i]==playerSign  and board[i + 6] != computerSign:
            return i + 6
        elif board[i + 6] == board[i]  and board[i]==playerSign and board[i + 3] != computerSign:
            return i + 3
        elif board[i+3] == board[i + 6]  and board[i+6]==playerSign and board[i] != computerSign:
            return i
    # ukos \
    if board[0] == board[4]  and board[0] == playerSign and board[8] != computerSign:
        return 8
    elif board[0] == board[8]  and board[0] == playerSign and board[4] != computerSign:
        return 4
    elif board[8] == board[4]  and board[4] == playerSign and board[0] != computerSign:
        return 0
    # ukos /
    if board[2] == board[4] and board[2] == playerSign and board[6] != computerSign:
        return 6
    elif board[2] == board[6] and board[2] == playerSign and board[4] != computerSign:
        return 4
    elif board[6] == board[4] and board[4] == playerSign and board[2] != computerSign:
        return 2
    return False

def computerLogicAttack(board):
    for i in range(3):
        # poziom
        if board[3 * i] == board[3 * i + 1] and board[3*i]==computerSign and board[3 * i + 2] != playerSign:
            return 3 * i + 2
        elif board[3 * i + 2] == board[3 * i + 1]  and board[3*i+1]==computerSign and board[3 * i] != playerSign:
            return 3 * i
        elif board[3 * i] == board[3 * i + 2]  and board[3*i]==computerSign and board[3 * i + 1] != playerSign:
            return 3 * i + 1
        # pion
        if board[i + 3] == board[i] and board[i]==computerSign  and board[i + 6] != playerSign:
            return i + 6
        elif board[i + 6] == board[i]  and board[i]==computerSign and board[i + 3] != playerSign:
            return i + 3
        elif board[i+3] == board[i + 6]  and board[i+6]==computerSign and board[i] != playerSign:
            return i
    # ukos \
    if board[0] == board[4]  and board[0] == computerSign and board[8] != playerSign:
        return 8
    elif board[0] == board[8]  and board[0] == computerSign and board[4] != playerSign:
        return 4
    elif board[8] == board[4]  and board[4] == computerSign and board[0] != playerSign:
        return 0
    # ukos /
    if board[2] == board[4] and board[2] == computerSign and board[6] != playerSign:
        return 6
    elif board[2] == board[6] and board[2] == computerSign and board[4] != playerSign:
        return 4
    elif board[6] == board[4] and board[4] == computerSign and board[2] != playerSign:
        return 2
    return False


def computerLogic(board,counter):

    x=computerLogicAttack(board)
    if x!=False:
        return x
    x=computerLogicDefence(board)
    if x!=False:
        return x
    while True:
        if counter == 0:
            counter += 1
            return 4
        move = random.randrange(1, 10, 1)
        if move in makeListOfFreeFields(board):
            return move - 1

counter = 0
x = random.randrange(0, 10)
while True:
    if x%2 == 1:
        if isEnd(board):
            break
        board[computerLogic(board, counter)] = computerSign
        # board[computerMove(board,counter)]=computerSign
        counter += 1
        if isEnd(board):
            break
        printBoard(board)
        board[enterMove(board)] = playerSign
    else:
        printBoard(board)
        if isEnd(board):
            break
        board[enterMove(board)] = playerSign
        counter += 1
        if isEnd(board):
            break
        board[computerLogic(board, counter)] = computerSign
