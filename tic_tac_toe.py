# write your code here

current_turn = 'X'
next_turn = 'O'

def check_game(M,Pl):
    win = False
    player = set(Pl)
    #check_hor
    for i in M:
        if set(i) == player:
            win = True
    #check_vert
    for i in range(3):
        if {M[0][i],M[1][i], M[2][i]} == player:
           win = True
           
    #check_diag
    diag1 = {M[0][0], M[1][1], M[2][2]}
    diag2 = {M[2][0], M[1][1], M[0][2]}

    if diag1 == player or diag2 == player:
        win = True
        
    return win

def switch_turn():
    global current_turn, next_turn
    temp = current_turn
    current_turn = next_turn
    next_turn = temp


win_x = False
win_o = False

x_count = 0
o_count = 0
blank = 0

line1 = [' ', ' ', ' ']
line2 = [' ', ' ', ' ']
line3 = [' ', ' ', ' ']

game = [line1,
        line2,
        line3]

print("""
---------
|       |
|       |
|       |
---------""")

while True:  #main loop
        
    while True:  #loop until the input move is valid
        move = input().split(' ')
        i = int(move[0]) - 1
        j = int(move[1]) - 1
            
        if not(move[0].isdigit()) or not(move[1].isdigit()):
            print("You should enter numbers!")
            continue
                
        elif (i >= 3 or j >= 3):
            print("Coordinates should be from 1 to 3!")
            continue
                
        elif not(game[i][j] == ' '):
            print("This cell is occupied! Choose another one!")
        
        else:
            break
    
    game[i][j] = current_turn
    
    print(f"""
    ---------
    | {' '.join(line1)} |
    | {' '.join(line2)} |
    | {' '.join(line3)} |
    ---------
    """)

    win_x = check_game(game,'X')
    win_o = check_game(game,'O')

    if win_x:
        print('X wins')
        break
    elif win_o:
        print('O wins')
        break
    elif (line1+line2+line3).count(' ') == 0:
        print('Draw')
        break
    else:
        switch_turn()
    
    
        
    