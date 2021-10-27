import random
from colorama import Fore, init, Back, Style
from colorama.ansi import Fore
import datetime
def fill(XO,board,choose):
    while(True):
        if(choose==1):
            row = int(input("row = "))
        else:
            row=random.randint(0,2)
        if (row<=2 and row>=0) :
            if(choose==1):
                col=int(input("col = "))
            else:
                col=random.randint(0,2)
            if (col <= 2 and col >= 0):
                if (board[row][col] == ' '):
                    board[row][col] = XO
                    break
                else:
                    if(choose==1):
                        print("This cell is already full. choose the other")
            else:
                print("Col is out of range....Try again ")
        else:
            print("Row is out of range....Try again ")
def Print(board):
    init()
    print(Fore.WHITE+"\t    0\t    1\t    2\n")
    print(Fore.WHITE+"\t0  ",end=' ')
    if(board[0][0]=='X'):
        print(Fore.RED+board[0][0],end=' ')
    elif(board[0][0]=="O"):
        print(Fore.BLUE+board[0][0],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[0][1]=='X'):
        print(Fore.RED+board[0][1],end=' ')
    elif(board[0][1]=="O"):
        print(Fore.BLUE+board[0][1],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[0][2]=='X'):
        print(Fore.RED+board[0][2],end=' ')
    elif(board[0][2]=="O"):
        print(Fore.BLUE+board[0][2],end=' ')
    print('\n')
    print(Fore.WHITE+"\t -------+-------+-------\n")
    print(Fore.WHITE+"\t1  ",end=' ')
    if(board[1][0]=='X'):
        print(Fore.RED+board[1][0],end=' ')
    elif(board[1][0]=="O"):
        print(Fore.BLUE+board[1][0],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[1][1]=='X'):
        print(Fore.RED+board[1][1],end=' ')
    elif(board[1][1]=="O"):
        print(Fore.BLUE+board[1][1],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[1][2]=='X'):
        print(Fore.RED+board[1][2],end=' ')
    elif(board[1][2]=="O"):
        print(Fore.BLUE+board[1][2],end=' ')
    print('\n')
    print(Fore.WHITE+"\t -------+-------+-------\n")
    print(Fore.WHITE+"\t2  ",end=' ')
    if(board[2][0]=='X'):
        print(Fore.RED+board[2][0],end=' ')
    elif(board[2][0]=="O"):
        print(Fore.BLUE+board[2][0],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[2][1]=='X'):
        print(Fore.RED+board[2][1],end=' ')
    elif(board[2][1]=="O"):
        print(Fore.BLUE+board[2][1],end=' ')
    print(Fore.WHITE+"\t|  ",end=' ')
    if(board[2][2]=='X'):
        print(Fore.RED+board[2][2],end=' ')
    elif(board[2][2]=="O"):
        print(Fore.BLUE+board[2][2],end=' ')
    print('\n')
    print(Style.RESET_ALL)
def win(board):
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' '):
        return True
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' '):
        return True
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != ' '):
            return True
        elif (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != ' '):
            return True
    return False
a=datetime.datetime.now()
j=9
board = [[' ',' ',' '],
                [' ',' ',' '],
                   [' ',' ',' ']]
print("Enter the number of your sellection: ")
print("1. Two players")
print("2. one player")
choose=int(input())
if(choose == 1):
    player1,player2=input("Enter the name two players :").split(",")
    turn = random.randint(1,2)
    while(j != 0):
        if (turn == 1):
            print("It's ",player1,"'s turn (X)\n")
            XO = 'X'
            turn = 2
        else:
            print("It's ",player2,"'s turn (O)\n")
            XO = 'O'
            turn = 1
        fill(XO, board,choose)
        Print(board)
        j -= 1
        n = win(board)
        if (n == True):
            j = 0
    if (n == False):
        print("DRAW\n")
    else:
        if (turn == 1):
            print(player2," is WIN!!!\n")
        else:
            print(player1," is WIN!!!\n")
elif(choose==2):
    player1=input("Enter the name of player :")
    turn = random.randint(1,2)
    while(j != 0):
        if (turn == 2):
            print("It's ",player1,"'s turn (X)\n")
            XO = 'X'
            turn = 1
        else:
            XO = 'O'
            turn = 2
        fill(XO, board,turn)
        Print(board)
        j -= 1
        n = win(board)
        if (n == True):
            j = 0
    if (n == False):
        print("DRAW\n")
    else:
        if (turn == 2):
            print("Computer is WIN!!!\n")
        else:
            print(player1," is WIN!!!\n")
b=datetime.datetime.now()
c=b-a
print(int(c.total_seconds())," SECONDS")