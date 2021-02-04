#   A B C
# 1 0 0 0
# 2 0 0 0
# 3 0 0 0
#player1 = 1, player2 = 2



game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
def board():
    x = f"""
      A B C
    1 {game[0][0]} {game[0][1]} {game[0][2]}
    2 {game[1][0]} {game[1][1]} {game[1][2]}
    3 {game[2][0]} {game[2][1]} {game[2][2]}"""
    #print(x)
    return x
#print(game[1][1])
#print(board())
player1 = input("Enter your name player1. ")
player2 = input("Enter your name player2. ")
player1no = 1
player2no = 2
player = 1
playername = ""

def change_board(player_no, X, Y):
    game[X][Y] = player_no
    return

def zerocheck():
    if 0 in game[0]:
        x = 1
    if 0 in game[1]:
        x = 1
    if 0 in game[2]:
        x = 1
    else:
        x = 0

    return x

def win():
    win_condition = 0
    if (game[0][0] == game[1][1] & game[2][2] & game[0][0] != 0) or \
            (game[0][0] == game[1][0] & game[2][0] & game[0][0] != 0) or \
            (game[0][0] == game[0][1] & game[0][2] & game[0][0] != 0) or \
            (game[1][0] == game[1][1] & game[1][2] & game[1][0] != 0) or \
            (game[2][0] == game[2][1] & game[2][2] & game[1][0] != 0):
        win_condition = 1
    return win_condition



while True:
    if player == 1:
        playername = player1
    else:
        playername = player2
    if zerocheck() == 0:
        break
    print(board())
    position_input = input(f"Player{playername}: Enter the position. ")
    for i in position_input:
        if i == "A":
            ypos = 0
        elif i == "B":
            ypos = 1
        elif i == "C":
            ypos = 2
        if i == "1":
            xpos = 0
        elif i == "2":
            xpos = 1
        elif i == "3":
            xpos = 2
    change_board(player, xpos, ypos)
    if win() == 1:
        print(f"Player{playername} has won!")
        break
    if player == 1:
        player = 2
    else:
        player = 1



print(board())