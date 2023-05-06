def build_ship(num):
    ships = []
    for i in range(num):
        x = random.randint(0,10-1)
        y = random.randint(0,10-1)
        ship = (x,y)
        ships.append(ship)
    return ships
