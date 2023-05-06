def prepare_battlefield():
    ships = []
    for i in range(50):
        x = random.randint(0,10-1)
        y = random.randint(0,10-1)
        ship = (x,y)
        ships.append(ship)
    return ships

def create_board():
    board = [[0]*10 for i in range(10)]
    return board

def board_display(board):
    for i in board:
        print(*i)
        
def play_game(player):
    if player == 'Me':
        x = random.randint(0,10-1)
        y = random.randint(0,10-1)
        guess = (x,y)
        time.sleep(3)
        return guess
        
    else:
        x = int(input('Enter a positive single-digit integer '))
        y = int(input('Enter a positive single-digit integer '))
        guess = (x,y)
        return guess

def update_board(guess, board, ships):        
    if guess in ships:
        print('You hit my battleship!')
        board[guess[0]][guess[1]] = 'X'
        ships.remove(guess)
        return board
    else:
        print('What a miss')
        board[guess[0]][guess[1]] = 'M'
        return board

def player_to_begin(player1, player2):
    player = random.randint(0,1)
    if player == 0:
        player = player1
        print("player1 begins")
        return player
    else:
        player = player2
        print("player2 begins")
        return player

def determine_player_turn(player, guess, ships):
    if guess in ships:
        if player == player1:
            player = player1
            print("player1's turn")
            return player
        else:
            player = player2
            print("player2's turn")
            return player
    else:
        if player == player1:
            player = player2
            print("player2's turn")
            return player
        else:
            player = player1
            print("player1's turn")
            return player
        
def first_move(player):
    if player == 'Me':
        x = random.randint(0,10-1)
        y = random.randint(0,10-1)
        guess = (x,y)
        time.sleep(3)
        return guess
    else:
        x = int(input('Enter a positive single-digit integer '))
        y = int(input('Enter a positive single-digit integer '))
        guess = (x,y)
        return guess

        

def determine_winner(player1_hits, player2_hits, initial_opponent_ships):
    player1_score = (player1_hits/initial_opponent_ships) *100
    player2_score = (player2_hits/initial_opponent_ships) *100
    if player1_score > player2_score:
        print('player1 score is ',player1_score)
        print('player2 score is ',player2_score)
        print('player1 wins')
    elif player1_score == player2_score:
        print('player1 score is ',player1_score)
        print('player2 score is ',player2_score)
        print('It is a draw')
    else:
        print('player1 score is ',player1_score)
        print('player2 score is ',player2_score)
        print('player2 wins')


    
import time
import random
##'Me' is the player_name for this computer
##Any other player_name will play by keyboard input
##Players are required to have different names
player1 = 'Evan' 
player2 =  'You'
player1_battlefield = prepare_battlefield()
player2_battlefield = prepare_battlefield()
initial_opponent_ships = len(player2_battlefield)
player1_board = create_board()
player2_board = create_board()
start_time = int(time.time())
end_time = start_time + 300
## player to make first move is picked randomly.
if time.time() < end_time:
   player = player_to_begin(player1, player2)
if player == player1:
    board = player1_board
    ships = player2_battlefield
    guess = first_move(player)
    board_display(update_board(guess, board, ships))
else:
    board = player2_board
    ships = player1_battlefield
    guess = first_move(player)
    board_display(update_board(guess, board, ships))

time_now = int(time.time())
while time_now < end_time:
    if len(player1_battlefield) > 0 and len(player2_battlefield) > 0:
        player = determine_player_turn(player, guess, ships)
        if player == player1:
            board = player1_board
            ships = player2_battlefield
            
        else:
            board = player2_board
            ships = player1_battlefield
            
        guess = play_game(player)
        board_display(update_board(guess, board, ships))

    else:
        break
    time_now = int(time.time())
print("GAME OVER!!")
player1_hits = initial_opponent_ships - len(player2_battlefield)
player2_hits = initial_opponent_ships - len(player1_battlefield)
determine_winner(player1_hits, player2_hits, initial_opponent_ships)
quit()

