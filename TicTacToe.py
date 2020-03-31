"""
# Board
# Display Board
# play Game
  -> Handle Turn
# Check Win
  -> Check Row
  -> Check Column
  -> Check Diagonals
# check Tie
# Flip Player

"""

# -------Global Variables-----

# game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game Started
Game_Still_Going = True

# Win Or Tie
Winner = None

# Current Player (Start's With 'x')
Current_Player = 'X'


# ----Global Variables Declaration End Hear----


# Displays The Board
def display_board():
    print("   TIC TAC TOE    ")
    print(" -----------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " |")
    print(" -----------------")
    print("| ", board[3], " | ", board[4], " | ", board[5], " |")
    print(" -----------------")
    print("| ", board[6], " | ", board[7], " | ", board[8], " |")
    print(" -----------------")


# Game Start's Hear
def play_game():
    while Game_Still_Going:
        # Play The Game
        handle_turn(Current_Player)

        # Check If Game Is Over
        check_is_gameover()

        # Flip The Other Player Turn
        flip_player()

        # Winner
    if Winner == "O" or Winner == "X":
        print()
        print("----Game Is Over----")
        display_board()
        print(Winner + " Won.")
    else:
        print(" Tie.")


# Event Handlar
def handle_turn(player):
    # Display The Current Board
    display_board()

    is_valid_position = True
    print(player, "'s Turn ")

    while is_valid_position:

        position = input("Enter The Position 1-9:")
        position = int(position) - 1

        if position < 0 or 8 < position or board[position] != '-':
            print("Position Is Not Valid")
            continue

        if player == 'X':
            board[position] = 'X'
            is_valid_position = False
        else:
            board[position] = 'O'
            is_valid_position = False


# Checks Weather Game Ended Or Not
def check_is_gameover():
    check_for_winner()
    check_if_tie()


# Checks For Winner
def check_for_winner():
    global Game_Still_Going
    global Winner

    # Check For Rows
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        Game_Still_Going = False
        if row1:
            Winner = board[0]
        elif row2:
            Winner = board[3]
        else:
            Winner = board[6]

    # Check For Columns
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        Game_Still_Going = False
        if col1:
            Winner = board[0]
        elif col2:
            Winner = board[1]
        else:
            Winner = board[2]

    # Check For Diagonals
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        Game_Still_Going = False
        if diagonal1:
            Winner = board[0]
        else:
            Winner = board[2]


# Checks Weather Tie Or Not
def check_if_tie():
    global Game_Still_Going
    if "-" not in board:
        Game_Still_Going = False


# Flipping The Player
def flip_player():
    global Current_Player
    if Current_Player == 'O':
        Current_Player = 'X'
    else:
        Current_Player = 'O'


# Main Call
play_game()


'''

   TIC TAC TOE    
 -----------------
|  -  |  -  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
X 's Turn 
Enter The Position 1-9:1

   TIC TAC TOE    
 -----------------
|  X  |  -  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
O 's Turn 
Enter The Position 1-9:2

   TIC TAC TOE    
 -----------------
|  X  |  O  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
X 's Turn 
Enter The Position 1-9:5

   TIC TAC TOE    
 -----------------
|  X  |  O  |  -  |
 -----------------
|  -  |  X  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
O 's Turn 
Enter The Position 1-9:3
 
   TIC TAC TOE    
 -----------------
|  X  |  O  |  O  |
 -----------------
|  -  |  X  |  -  |
 -----------------
|  -  |  -  |  -  |
 -----------------
X 's Turn 
Enter The Position 1-9:9

----Game Is Over----

   TIC TAC TOE    
 -----------------
|  X  |  O  |  O  |
 -----------------
|  -  |  X  |  -  |
 -----------------
|  -  |  -  |  X  |
 -----------------
X Won.



'''
