import time
import random

def build_board():
    board = [[0]*10 for i in range(10)]
    return board

def print_board(board):
    for i in build_board():
        print(*i)

def build_ship(num):
    ships = []
    for i in range(num):
        x = random.randint(0,10-1)
        y = random.randint(0,10-1)
        ship = (x,y)
        ships.append(ship)
    return ships

def player_guess():
    guesses = []
    x = int(input())
    y = int(input())
    guess = (x,y)
    guesses.append(guess)
    print(guesses)
    return guess

def timer(Time):
   start_time = time.time()
   print('Game starts now',start_time)
   end_time = Time + start_time
   return end_time

def update_board():
    if player_guess() in build_ship() and player_guess() not in guesses:
        print('You hit my battleship!')
        build_board()[guess[0]][guess[1]] = 'X'
        build_ship().remove(guess)
        guesses.append(player_guess())
        return board
    elif player_guess() not in build_ship() and player_guess() not in guesses:
        print('What a miss')
        build_board()[guess[0]][guess[1]] = 'M'
        guesses.append(player_guess())
        return board
    else:
        print('You already made that guess')
        return board
    
def destroyed_ships_ratio():
    total_ships = len(build_ship())
    if time.time() == start_time:
        a = total_ships
    elif time.time() == end_time:
        b = total_ships
    destroyed_ships = a-b
    destroyed_ships_ratio = (destroyed_ships//a)*100
    return destroyed_ships_ratio
        
def play_game():
    print_board(build_board)
    build_ship(9)
    while time.time()< timer(5):
        player_guess
        update_board
        print_board(update_board)
    destroyed_ships_ratio
    print('Game Over'+'\n'+'You destroyed {destroyed_ships_ratio} of enemy ships')
    
play_game()   



