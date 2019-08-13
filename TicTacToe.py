#Tic Tac Toc 1 Human VS Computer
import random
N=5
pos=[i for i in range(N**2)]

def printBoard(board):
    for i in range(N):
        if(i!=0):
            print("-----"*N)
        for j in range(N):
            if j!=N-1:
                print(board[i][j],end=" | ")
            else:
                print(board[i][j])

    print("")

def isWinner(board,Symbol):
    row_Check = Column_Check = UpperDiagonalCheck = LowerDiagonalCheck = 0
    #Checking The Row Sentinel
    for i in range(N):
        row_Check=0
        for j in range(N):
            if board[i][j]==Symbol:
                row_Check+=1
        if row_Check==N:
            print("Won By Row Check -> ",i)
            return True
    #Checking Column Sentinel
    for i in range(N):
        Column_Check=0
        for j in range(N):
            if board[j][i]==Symbol:
                Column_Check +=1
        if Column_Check==N:
            print("Won By Column Check -> ", i)
            return True
    #Checking Lower Diagonal

    for i,j in zip(range(0,N,1),range(0,N,1)):
        if board[i][j]==Symbol:
            LowerDiagonalCheck+=1
        if LowerDiagonalCheck==N:
            print("Won By LowerDiagonal Check ")
            return True
    #Checking Upper Diagonal Sentinel
    for i, j in zip(range(N - 1, -1, -1), range(0, N, 1)):
        if board[i][j]==Symbol:
            UpperDiagonalCheck+=1
        if UpperDiagonalCheck==N:
            print("Won By UpperDiagonal Check ")
            return True

    return False #If All The Above Cases Are Failed

def HumanVsComputer():
    Remaning_To_Fill=N*N
    Human_Symbol=input('Select Your Symbol (O/X):')
    if Human_Symbol=='O':
        Computer_Symbol='X'
    else:
        Computer_Symbol='O'
    board=[[-1 for i in range(N)]for i in range(N)]
    printBoard(board)
    choice=input('Do You Want To Start:(Y/N)')
    while Remaning_To_Fill:
        if choice=='Y':
            choice=1
            print("Human's Choice")
            print("Select Your Position Choice From Available Positions")
            print(pos)
            while(1):
                Selected_Position=int(input())
                if Selected_Position not in pos:
                    print("Invalid Position, Try Again!!!")
                elif Selected_Position in pos:
                    pos.remove(Selected_Position)
                    row = Selected_Position //N
                    column = Selected_Position % N
                    board[row][column]=Human_Symbol
                    Remaning_To_Fill -= 1
                    printBoard(board)
                    break
            if isWinner(board,Human_Symbol):
                print("Human Won the Match")
                return
        if choice!='Y':
            choice='Y'
            print("Computer's Choice")
            Selected_Position=random.choice(pos)
            pos.remove(Selected_Position)
            row=Selected_Position//N
            column=Selected_Position%N
            board[row][column]=Computer_Symbol
            Remaning_To_Fill -= 1
            printBoard(board)
            if isWinner(board,Computer_Symbol):
                print("Computer Won the Match")
                return
    if not Remaning_To_Fill :
        print("Draw Match")
HumanVsComputer()























