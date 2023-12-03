import json
import pandas as pd
import numpy as np
from player import player
from grid import grid
class game:
	def __init__(self, game_config_file):
		self.game_info = json.load(open(game_config_file))
		self.player_list = []
		self.player_list.append(player(0, grid(1,1), grid(1,1)))
	def setup_player(self, player_id):
		primary_grid = grid(self.game_info["grid"]["width"], self.game_info["grid"]["height"])
		target_grid = grid(self.game_info["grid"]["width"], self.game_info["grid"]["height"])
		p = player(player_id, primary_grid, target_grid)
		self.player_list.append(p)
	def setup_ship(self, player_id, ship_name, end_coords):
		# check list size
		if len(end_coords) != 2:
			return False
		# check list elements(end_coords)
		for x in end_coords:
			# check size of each coord
			if len(x) < 2 or len(x) > 3:
				return False
			# check if first char is alpha
			if not x[0].isalpha():
				return False
			# check is second char is numeric
			if not x[1].isnumeric():
				return False
			# check 10
			if len(x) == 3:
				if not x[1] == '1':
					return False
				if not x[2] == '0':
					return False
		# check if coords are within bounds
		setup_complete = self.player_list[player_id].add_ship(ship_name, self.game_info["ships"][ship_name], end_coords)
		if setup_complete:
			return True
		else:
			return False
	def valid_attack(self, coord):
		print(coord)
		# check size of coord
		if len(coord) < 2 or len(coord) > 3:
			return False
		# check if first char is alpha
		if not coord[0].isalpha():
			return False
		# check is second char is numeric
		elif not coord[1].isnumeric():
			return False
		# check if coords are within bounds of a-j
		list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		if not coord[0] in list_letters:
			return False
		# check 10
		if len(coord) == 3:
			if not coord[1] == '1':
				return False
			elif not coord[2] == '0':
				return False
		elif int(coord[1]) not in range(1,10):
			return False
		return True
     
	def turn(self, player_id, coordinate):
		if player_id == 1:
			hit = self.player_list[2].hit_ship(coordinate)
			if hit:
				self.player_list[1].target_grid.change_val(coordinate, "X")
			else:
				self.player_list[1].target_grid.change_val(coordinate, "O")
			return hit
		elif player_id == 2:
			hit = self.player_list[1].hit_ship(coordinate)
			if hit:
				self.player_list[2].target_grid.change_val(coordinate, "X")
			else:
				self.player_list[2].target_grid.change_val(coordinate, "O")
			return hit
		else:
			print("[Game] 3 or more players not supported!")
			return False
	def print_grid(self, player_id):
		self.player_list[player_id].target_grid.print_grid()
		print()
		self.player_list[player_id].primary_grid.print_grid()
	def game_over(self):
		for player in self.player_list:
			if player.player_id == 0:
				pass
			elif player.defeated():
				return True
		return False
