from game import game
import time

#print(game.__file__)
mygame = game("game-config.json")

mygame.setup_player(1)
mygame.setup_player(2)

ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(1, "Aircraft Carrier", ["A1", "A5"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(1, "Battleship", ["B2", "B5"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(1, "Destroyer", ["C1", "C3"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(1, "Submarine", ["D4", "D6"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(1, "Patrol Boat", ["J5", "J6"])

mygame.print_grid(1)

ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(2, "Aircraft Carrier", ["A1", "E1"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(2, "Battleship", ["B2", "E2"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(2, "Destroyer", ["C6", "E6"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(2, "Submarine", ["I5", "G5"])
ship_set = False
while not ship_set:
	ship_set = mygame.setup_ship(2, "Patrol Boat", ["A9", "B9"])

mygame.print_grid(2)

hit = mygame.turn(1, "A5")
if hit:
	if mygame.game_over():
		print("Bruh")
else:
	if mygame.game_over():
		print("Bruh")



