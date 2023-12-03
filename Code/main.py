import time
import json
import game

msg_delay = 1.0
msg_delay_2 = 2.0
msg_delay_3 = 4.0

###################################################
# Intro
###################################################

print("\033c", end='')
print("Battleship - CMD Version")
print("   Game developed by Yusra, Karol, Bilal, Darshan")
print("")
print("Help: ")
print("	  Use the terminal to input coordinates of where you want to place your ships")
print("   When the game starts, input the coordinate you want to attack")
print("   Take down all enemy ships and win the war!!!")
time.sleep(msg_delay)
print("")
print("   For more information, click How-To-Play: https://www.wikihow.com/Play-Battleship")
print("")
print("Info:")
print("   To enter coordinates, type in this format: (a-j)(1-10) (a-j)(1-10) ex. a3 d3")
print()
print()
print()
print("Loading game in few seconds...")
time.sleep(msg_delay_2)
# print("\033c", end='')



print("[Operator] Remote terminal activated...")
print("")
time.sleep(msg_delay)
print("[Operator] Input # of players:", end=' ', flush=True)
time.sleep(msg_delay)
print("2")
print("[Operator] 2 players selected...")
print()
time.sleep(msg_delay_2)
print("[Operator] Satellite link established...")
print()
time.sleep(msg_delay)
print("[Operator] Input game option:", end=' ', flush=True)
time.sleep(msg_delay)
print("1")
print("[Operator] Classic mission selected...")
print()
time.sleep(msg_delay_2)
print("\033c", end='')

###################################################
# Game and Player Setup
###################################################

# Get list of all ships
lst = json.load(open("Code/game-config.json"))
ships = lst["ships"].keys()

# Create game
mygame = game.game("Code/game-config.json")

# Player 1 enters ship coordinates
print("[Operator] Player 1, enter please configuration: ", end='', flush=True)
time.sleep(msg_delay_2)
print("1")
print("[Operator] Custom configuration selected...")
time.sleep(msg_delay_2)
print("")
mygame.setup_player(1)
for ship in ships:
	print("[Control Tower]", ship, "recording!")
	res = input("[Operator] Enter coordinates: ")
	res = res.upper()
	print(res)
	split_res = res.split()
	is_res_valid = mygame.setup_ship(1, ship, split_res)
	while is_res_valid == False:
		print("[Operator] Incorrect coordinates...")
		res = input("[Operator] Enter coordinates: ")
		res = res.upper()
		split_res = res.split()
		is_res_valid = mygame.setup_ship(1, ship, split_res)
	print("[Operator]", ship,"\"", res, "\" selected...")
	print("")
	mygame.print_grid(1)
time.sleep(msg_delay)
print("\033c", end='')

# Player 2 ship configurations
print("[Operator] Player 2, enter please configuration: ", end='', flush=True)
time.sleep(msg_delay_2)
print("1")
print("[Operator] Custom configuration selected...")
time.sleep(msg_delay_2)
print("")
mygame.setup_player(2)
for ship in ships:
	print("[Control Tower]", ship, "recording!")
	res = input("[Operator] Enter coordinates: ")
	res = res.upper()
	split_res = res.split()
	is_res_valid = mygame.setup_ship(2, ship, split_res)
	while is_res_valid == False:
		print("[Operator] Incorrect coordinates...")
		res = input("[Operator] Enter coordinates: ")
		res = res.upper()
		split_res = res.split()
		is_res_valid = mygame.setup_ship(2, ship, split_res)
	print("[Operator]", ship,"\"", res, "\" selected...")
	print("")
	mygame.print_grid(2)
time.sleep(msg_delay)
print("\033c", end='')

###################################################
# Gameplay
###################################################

player_turn = 1
while True:
	# Player 1 turn
	mygame.print_grid(player_turn)
	print()
	res = input("[Operator] Player 1, Enter target coordinates: ")
	res = res.upper()
	valid_res = mygame.valid_attack(res)
	while valid_res == False:
		print("[Operator] Incorrect coordinates...")
		res = input("[Operator] Enter coordinates: ")
		res = res.upper()
		split_res = res.split()
		valid_res = mygame.valid_attack(res)
	hit = mygame.turn(player_turn, res)
	if hit:
		print("[Operator] Ship hit at", res, "!")
		if mygame.game_over():
			print("\033c", end='')
			break
	else:
		print("[Operator] Miss at", res, ".")
	time.sleep(msg_delay)
	print("\033c", end='')
	
	# Player 2 turn
	player_turn = 2
	mygame.print_grid(player_turn)
	print()
	res = input("[Operator] Player 2, Enter target coordinates: ")
	res = res.upper()
	valid_res = mygame.valid_attack(res)
	while valid_res == False:
		print("[Operator] Incorrect coordinates...")
		res = input("[Operator] Enter coordinates: ")
		res = res.upper()
		split_res = res.split()
		valid_res = mygame.valid_attack(res)
	hit = mygame.turn(player_turn, res)
	if hit:
		print("[Operator] Ship hit at", res, "!")
		if mygame.game_over():
			print("\033c", end='')
			break
	else:
		print("[Operator] Miss at", res, ".")
	time.sleep(msg_delay)
	print("\033c", end='')
	player_turn = 1

print("[Operator] Game over!")
print()
print("[Operator] Player", player_turn, "wins!")
time.sleep(msg_delay_2)
print("\033c", end='')
