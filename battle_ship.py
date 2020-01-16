import random
import time
upper_board={}
lower_board={}
for i in range(1,17):
    upper_board[i]=str(i)
    lower_board[i]=str(i)
possible_hides=[]
for i in range(1,17):
    possible_hides.append(str(i))
possible_battleship_moves=[]
possible_computer_moves=[]
for i in range(1,17):
    possible_battleship_moves.append(str(i))
    possible_computer_moves.append(i)
boss_hits=[]
hide_previous_choices=[]



battle_ship_moves=[]
last_boss_hide=[]
yellow_numbers=[1,4,13,16]
green_numbers_row_1=[2,3]
green_numbers_row_2=[14,15]
green_numbers_column_1=[5,9]
#green_numbers_column_2=[9,12]
blue_numbers=[6,7,10,11]
boss_hit_tally=[]
while boss_hit_tally>0:
    if len(battle_ship_moves)<1:
        computer_hide=random.randint(1,17)
        last_boss_hide.append(computer_hide)
        battle_ship_moves.append(1)
    else:
        possible_computer_hide=[]
        if last_boss_hide[0] in blue_numbers:
            possible_computer_hide.append(last_boss_hide[0]+1)
            possible_computer_hide.append(last_boss_hide[0]-1)
            possible_computer_hide.append(last_boss_hide[0]+4)
            possible_computer_hide.append(last_boss_hide[0]-4)
            possible_computer_hide.append(last_boss_hide[0])
        elif last_boss_hide[0] in yellow_numbers:
            if last_boss_hide[0]==1:
                possible_computer_hide.append(1)
                possible_computer_hide.append(2)
                possible_computer_hide.append(5)
            elif last_boss_hide[0]==13:
                possible_computer_hide.append(13)
                possible_computer_hide.append(9)
                possible_computer_hide.append(14)
            elif last_boss_hide[0]==16:
                possible_computer_hide.append(16)
                possible_computer_hide.append(15)
                possible_computer_hide.append(12)
            else:
                possible_computer_hide.append(4)
                possible_computer_hide.append(3)
                possible_computer_hide.append(8)
        else:
            if last_boss_hide[0] in green_numbers_row_1:
                possible_computer_hide.append(last_boss_hide[0]+1)
                possible_computer_hide.append(last_boss_hide[0]-1)
                possible_computer_hide.append(last_boss_hide[0]+4)
                possible_computer_hide.append(last_boss_hide[0])
            elif last_boss_hide[0] in green_numbers_row_2:
                possible_computer_hide.append(last_boss_hide[0]+1)
                possible_computer_hide.append(last_boss_hide[0]-1)
                possible_computer_hide.append(last_boss_hide[0]-4)
                possible_computer_hide.append(last_boss_hide[0])
            elif last_boss_hide[0] in green_numbers_column_1:
                possible_computer_hide.append(last_boss_hide[0]+1)
                possible_computer_hide.append(last_boss_hide[0]+4)
                possible_computer_hide.append(last_boss_hide[0]-4)
                possible_computer_hide.append(last_boss_hide[0])
            else:
                possible_computer_hide.append(last_boss_hide[0]-1)
                possible_computer_hide.append(last_boss_hide[0]+4)
                possible_computer_hide.append(last_boss_hide[0]-4)
                possible_computer_hide.append(last_boss_hide[0])
        while True:
            computer_hide = random.choice(possible_computer_hide)
            print(computer_hide)
            print(possible_computer_hide)
            print(last_boss_hide)
            if upper_board[computer_hide]=="X":
                continue
            elif upper_board[computer_hide]==" X":
                continue
            else:
                last_boss_hide.clear()
                last_boss_hide.append(computer_hide)
                break
        #print(computer_hide)
    board2()
    hide_choice=input("Where would you like to hide?: ")
    while True:
        if hide_choice in possible_hides:
            hide_previous_choices.append(hide_choice)
            if len(hide_previous_choices)>1:
                lower_board[int(hide_previous_choices[len(hide_previous_choices)-2])]= str(hide_previous_choices[len(hide_previous_choices)-2])
                break
        else:
            hide_choice=input("That space is not available. Please select again: ")
    if int(hide_choice)<10:
        lower_board[int(hide_choice)]="+"
    else:
        lower_board[int(hide_choice)]=" +"
    board2()
    battleship_move=input("Where would you like to attack?: ")
    while True:
        if battleship_move in possible_battleship_moves:
            possible_battleship_moves.remove(battleship_move)
            break
        else:
            battleship_move=input("That space is not available. Please select again: ")
    if int(battleship_move)==computer_hide:
        boss_hit_tally.append(1)
        clear_board()
        battle_ship_moves.clear()
        last_boss_hide.clear()
    else:
        if int(battleship_move)<10:
            upper_board[int(battleship_move)]="X"
        else:
            upper_board[int(battleship_move)]=" X"
        computer_move=random.randint(1,17)
        while True:
            if computer_move in possible_computer_moves:
                if computer_move==int(hide_choice):
                    print("\n"*40+"Oh no!!! The Boss has hit you!!!\n")
                    character.lives_lost()
                    time.sleep(5)
                    clear_board()
                    battle_ship_moves.clear()
                    last_boss_hide.clear()
                    break
                else:
                    possible_computer_moves.remove(computer_move)
                    possible_hides.remove(str(computer_move))
                    if computer_move<10:
                        lower_board[computer_move]="X"
                    else:
                        lower_board[computer_move]=" X"
                    break
            else:
                computer_move=random.randint(1,17)
def board2():


    print("\n"*40)
    print(" "*4+"THE BOSS")
    print("-"*16)
    for i in range(1,5):
        print("|"+upper_board[i]+" |",end="")
    print("\n"+"-"*16)
    for i in range(5,9):
        print("|"+upper_board[i]+" |",end="")
    print("\n"+"-"*16)
    print("|"+upper_board[9]+" |",end="")
    for i in range(10,13):
        print("|"+upper_board[i]+"|",end="")
    print("\n"+"-"*16)
    for i in range(13,17):
        print("|"+upper_board[i]+"|",end="")
    print("\n"+"-"*16)
    print("\n"+"-"*16)
    print("\n"+"-"*16)
    for i in range(13,17):
        print("|"+lower_board[i]+"|",end="")
    print("\n"+"-"*16)
    print("|"+lower_board[9]+" |",end="")
    for i in range(10,13):
        print("|"+lower_board[i]+"|",end="")
    print("\n"+"-"*16)
    for i in range(5,9):
        print("|"+lower_board[i]+" |",end="")
    print("\n"+"-"*16)
    for i in range(1,5):
        print("|"+lower_board[i]+" |",end="")
    print("\n"+"-"*16)
    print(" "*5+str(character.name))

def clear_board():
    upper_board.clear()
    lower_board.clear()
    possible_hides.clear()
    possible_battleship_moves.clear()
    possible_computer_moves.clear()
    for i in range(1,17):
        upper_board[i]=str(i)
        lower_board[i]=str(i)
        possible_hides.append(str(i))
        possible_battleship_moves.append(str(i))
        possible_computer_moves.append(i)

