#-----------------------------
from operator import truediv
import colorama             #-
from colorama import Fore   #-
import random               #-
#-----------------------------

#----------------------------------------------------------------
X = "X"                                                        #-
O = "O"                                                        #-
player_1 = 0                                                   #-
player_2 = 0                                                   #-
cols = 3                                                       #-
rows = 3   
move = 1                                                    #-                        
pos = [[' ' for i in range(cols)] for j in range(rows)]        #-
#----------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
def initialize():
    global pos,rows,cols,move
    move = 1
    for i in range(3):
        for j in range (3):
            for rows in pos:
                for cols in rows:
                    pos[i][j]=' '    # initialising the board

def set_marker():
    global player_1,player_2
    print("")
    print(f"{Fore.CYAN}Player 1 select your marker")
    marker=input("X or O : ")
    print("")
    if marker == X or marker == "x" :
        player_1 = X
        player_2 = O
    elif marker == O  or marker == "o":    # assigning the marker
        player_1 = O
        player_2 = X
    else:
        print(f"{Fore.RED}-----------------------------------------------")
        print("Error!!! enter correct input")
        print("-----------------------------------------------")
        set_marker()

def win():
    global pos 
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))

    for a, b, c in wins:
        ia , ja = num_to_ij(a)
        ib , jb = num_to_ij(b)
        ic , jc = num_to_ij(c)
        chars = pos[ia][ja] + pos[ib][jb] + pos[ic][jc]
        if chars == "XXX" or chars == "OOO":
            return True
    return False

def tie():
    global pos
    count = 0
    for i in range (3):
        for j in range (3):
            if pos[i][j] == X or pos[i][j] == O:
                count+=1
    if count == 9:
        return True
    return False

def board():
    global pos
    print(f"{Fore.LIGHTMAGENTA_EX}")
    print("\t",pos[0][0],"|",pos[0][1],"|",pos[0][2])
    print("\t --------- ")
    print("\t",pos[1][0],"|",pos[1][1],"|",pos[1][2])
    print("\t --------- ")
    print("\t",pos[2][0],"|",pos[2][1],"|",pos[2][2])
    print("")

def num_to_ij(num):
    i=-1
    j=-1
    if num >=0 and num<=2:
        i=0
        j=num
    elif num >=3 and num<=5:
        i=1
        j=num-3
    else:
        i=2
        j=num-6
    return i,j

def row_check(i):
    global pos
    for j in range (3):
        if pos[i][j] == ' ':
            fill(i,j)

def col_check(j):
    global pos
    for i in range (3):
        if pos[i][j] == ' ':
            fill(i,j)

def fill(i,j):
    global pos,player_2,rows,cols
    for rows in pos:
            for cols in rows:
                pos[i][j] = player_2

def dia_check_1():
    global pos
    if pos[0][0] == ' ':
        fill(0,0)
    elif pos[1][1] == ' ':
        fill(1,1)
    elif pos[2][2] == ' ':
        fill(2,2)

def dia_check_2():
    global pos,player_2
    if pos[0][2] == ' ':
        fill(0,2)
    elif pos[1][1] == ' ':
        fill(1,1)
    elif pos[2][0] == ' ':
        fill(2,0)

def check(num):
    global pos
    i , j = num_to_ij(num)
    if pos[i][j] == ' ':
        return True
    return False    

def rand(n):
    global pos,player_2
    if pos[0][0] == ' ':
        fill(0,0)
        comp_move(n)
    elif pos[0][2] == ' ':
        fill(0,2)
        comp_move(n)
    elif pos[2][0] == ' ':
        fill(2,0)
        comp_move(n)
    elif pos[2][2] == ' ':
        fill(2,2)
        comp_move(n)
    else:
        for i in range (3):
            for j in range (3):
                if pos[i][j] == ' ':
                    pos[i][j] = player_2
                    comp_move(n)

def row_input():
    global pos 
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    count = 0
    for a, b, c in wins:
        ia , ja = num_to_ij(a)
        ib , jb = num_to_ij(b)
        ic , jc = num_to_ij(c)
        chars = pos[ia][ja] + pos[ib][jb] + pos[ic][jc]
        if chars == "XX " or chars == "OO " or chars == "X X" or chars == "O O" or chars == " XX" or chars == " OO":
            row_check(count)
            return True
        count+=1
    return False

def col_input():
    global pos 
    wins = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
    count = 0
    for a, b, c in wins:
        ia , ja = num_to_ij(a)
        ib , jb = num_to_ij(b)
        ic , jc = num_to_ij(c)
        chars = pos[ia][ja] + pos[ib][jb] + pos[ic][jc]
        if chars == "XX " or chars == "OO " or chars == "X X" or chars == "O O" or chars == " XX" or chars == " OO":
            col_check(count)
            return True
        count+=1
    return False

def dia_input():
    global pos 
    wins = ((0, 4, 8), (2, 4, 6))
    count = 1
    for a, b, c in wins:
        ia , ja = num_to_ij(a)
        ib , jb = num_to_ij(b)
        ic , jc = num_to_ij(c)
        chars = pos[ia][ja] + pos[ib][jb] + pos[ic][jc]
        if chars == "XX " or chars == "OO " or chars == "X X" or chars == "O O" or chars == " XX" or chars == " OO":
            if count == 1:
                dia_check_1()
            else:
                dia_check_2()
            return True
        count+=1
    return False
    
def comp_move(n):
    board()
    if win():
        print("")
        print(f"{Fore.LIGHTGREEN_EX}-----------------------------------------------")
        print("Computer won :)")
        print("-----------------------------------------------")
        menu()
    elif tie():
        print("")
        print(f"{Fore.LIGHTGREEN_EX}-----------------------------------------------")
        print("Tied!!!")
        print("-----------------------------------------------")
        menu()
    else:
        user_input(n)

def comp_input(n):
    global pos,player_2
    print("")
    print(f"{Fore.YELLOW}-----------------------------------------------")
    print("After Computer move") 
    print("-----------------------------------------------")
    print("")
    if row_input():
        comp_move(n)
    elif col_input():
        comp_move(n)
    elif dia_input():
        comp_move(n)
    else:
        rand(n)

def user_input(n):
    global pos,player_1,rows,cols,move
    print(f"{Fore.CYAN}Enter the postion no. for your marker")
    num = int(input("1 to 9 : "))
    num=num-1
    if num <= 8 and num >= 0:

        if check(num):
            i , j = num_to_ij(num)
            for rows in pos:
                for cols in rows:
                    if n == 1:
                        pos[i][j]=player_1
                    elif n == 2 and move%2 != 0 :
                        pos[i][j]=player_1
                        move=move+1
                    elif n == 2 and move%2 == 0 :
                        pos[i][j]=player_2
                        move=move+1
            print(f"{Fore.YELLOW}-----------------------------------------------")
            if n == 1:
                print("After Player 1 move")
            elif n == 2 and move%2 == 0:
                print("After Player 1 move")
            else :
                print("After Player 2 move")
            print("-----------------------------------------------")
            board()
            if win():
                print("")
                print(f"{Fore.LIGHTGREEN_EX}-----------------------------------------------")
                if n == 1:
                    print("Player 1 won :(")
                elif n == 2 and move%2 == 0 :
                    print("Player 1 won :)")
                elif n == 2 and move%2 != 0 :
                    print("Player 2 won :)")
                print("-----------------------------------------------")
                menu()
            elif tie():
                print("")
                print(f"{Fore.LIGHTGREEN_EX}-----------------------------------------------")
                print("Tied!!!")
                print("-----------------------------------------------")
                menu()
            else:
                if n == 1:
                    comp_input(n)
                else:
                    user_input(n)

        else:
            print(f"{Fore.RED}-----------------------------------------------")
            print("Error!!! already filled try again")
            print("-----------------------------------------------")
            user_input(n)

    else:
        print(f"{Fore.RED}-----------------------------------------------")
        print("Error!!! position does not exist!")
        print("-----------------------------------------------")
        user_input(n)
        
    

def instructions():
    print("\t\t\t  Tic-Tac-Toe\n\n")
    print("Choose a cell numbered from 1 to 9 as below and play\n\n")
    print("\t\t\t  1 | 2  | 3  \n")
    print("\t\t\t--------------\n")
    print("\t\t\t  4 | 5  | 6  \n")
    print("\t\t\t--------------\n")
    print("\t\t\t  7 | 8  | 9  \n\n")
    print("-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n\n")
    menu()

def dsplay():
    display = '''
        1 | 2 | 3   
        ---------    
        4 | 5 | 6    
        ---------    
        7 | 8 | 9   
        '''
    print(f"{Fore.YELLOW}-----------------------------------------------")
    print("The board with the position no. written in it")
    print("-----------------------------------------------")
    print(f"{Fore.CYAN}",display.format(*display))

def toss():
    n=random.randint(0,1)
    if n == 0:
        return True
    return False

def OX(n):
    global player_1,player_2,pos
    initialize()
    print(f"{Fore.YELLOW}-----------------------------------------------")
    print("Starting game ...") 
    print("-----------------------------------------------")
    set_marker()
    dsplay()
    if n == 1:
        if toss():
            print(f"{Fore.GREEN}-----------------------------------------------")
            print("Player 1 has won the toss !!!")
            print("-----------------------------------------------")
            user_input(n)
        else :
            print(f"{Fore.GREEN}-----------------------------------------------")
            print("Computer has won the toss !!!")
            print("-----------------------------------------------")
            comp_input(n)
    else :
        user_input(n)

def menu():
    print(f"{Fore.YELLOW}-----------------------------------------------")
    print("MAIN MENU") 
    print("-----------------------------------------------")
    print("")
    print("Enter\n1. To start a new game with bot \n2. To start a new game with player\n3. To read instructions\n4. To quit ")
    print("-----------------------------------------------")
    n = int(input("Input : "))
    if n == 1 or n == 2:
        OX(n)
    elif n == 3:
        instructions()
    elif n == 4:
        raise SystemExit
    else:
        print(f"{Fore.RED}-----------------------------------------------")
        print("Error!!! invalid input")
        print("-----------------------------------------------")
        print("")
        menu()

menu()
#--------------------------------------------------------------------------------------------------