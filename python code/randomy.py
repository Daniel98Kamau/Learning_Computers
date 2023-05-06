import time
import random

def build_board():
    board = [[0]*12 for i in range(12)]
    return board

def print_board(board):
    for i in build_board():
        print(*i)

def build_ship(num):
    ships = []
    for i in range(num):
        x = random.randint(0,12-1)
        y = random.randint(0,12-1)
        ship = (x,y)
        ships.append(ship)
    return ships

def play_game(Time):
    start_time = time.time()
    print(start_time)
    while time.time()- start_time < Time:
        guess_shoot
        print(guess_shoot())
        update_board
        print_board
    else:
        print('Game Over at', time.time())

def guess_shoot():
    x = int(input())
    y = int(input())
    shoot = (x,y)
    return shoot

def update_board(build_board):
    if guess_shoot() in build_ship(15): 
        build_board()[guess_shoot()[0]][guess_shoot()[1]] = 'X'
        ships.remove(shoot)
        if guess_shoot() not in guesses:
            guesses.append(shoot)
        return board
    else:
        build_board()[guess_shoot()[0]][guess_shoot()[1]] = 'M'
        if guess_shoot() not in guesses:
            guesses.append(shoot)
        return board

guesses = []
play_game(10)
