import grid
class ship:
	def __init__(self, kind, length, identifier, end_coords):
		self.kind = kind
		self.length = length
		self.identifier = identifier
		self.end_coordinates = end_coords
		self.coordinates = []
		self.health = []
	def setup(self):
		self.coordinates = self.gen_coords(self.end_coordinates)
		self.health = [self.identifier]*self.length
		if not self.coordinates:
			return False
		else:
			return True
	def gen_coords(self, end_coords):
		if any("10" in coord for coord in end_coords):
			if "10" in end_coords[0] and not "10" in end_coords[1]:
				end_coords[0], end_coords[1] = end_coords[1], end_coords[0]
		else:
			end_coords.sort()
		start = grid.convert_coord(end_coords[0])
		end = grid.convert_coord(end_coords[1])
		temp = []
		if start[1] < end[1] and start[0] == end[0]:
			ulen = end[1] - start[1] + 1
			if ulen != self.length:
				return temp
			for i in range(start[1], end[1]+1):
				temp.append(grid.rev_convert_coord(start[0], i))
		elif start[0] < end[0] and start[1] == end[1]:
			ulen = end[0] - start[0] + 1
			if ulen != self.length:
				return temp
			for i in range(start[0], end[0]+1):
				temp.append(grid.rev_convert_coord(i, start[1]))
		else:
			pass
		return temp
	def sink_part(self, coordinate):
		if coordinate in self.coordinates:
			i = self.coordinates.index(coordinate)
			if self.health[i] == self.identifier:
				self.health[i] = "!"
				return True
		return False
	def ship_sunk(self):
		if self.identifier in self.health:
			return False
		else:
			return True
