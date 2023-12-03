from grid import grid
from ship import ship
class player:
	def __init__(self, player_id, pg, tg):
		self.player_id = player_id
		self.primary_grid = pg
		self.target_grid = tg
		self.ships = []
		self.ship_peg_count = 0
		self.ship_peg_loss = 0
	def add_ship(self, ship_name, info, end_coords):
		s = ship(ship_name, info["length"], info["identifier"], end_coords)
		ready = s.setup()
		if ready:
			self.ship_peg_count = self.ship_peg_count + s.length
			for t in self.ships:
				if any(x in s.coordinates for x in t.coordinates):
					return False
			self.ships.append(s)
			for x in s.coordinates:
				self.primary_grid.change_val(x, s.identifier)
			return True
		return False
	def defeated(self):
		return self.ship_peg_loss == self.ship_peg_count
	def hit_ship(self, coord):
		for ship in self.ships:
			ship_did_sink = ship.sink_part(coord)
			if ship_did_sink:
				self.ship_peg_loss = self.ship_peg_loss + 1
				self.primary_grid.change_val(coord, "!")
				return ship_did_sink
