class grid:
	def __init__(self, y, x):
		self.grid = [["-" for x in range(x)] for y in range(y)]
		self.width = x
		self.height = y
	def print_grid(self):
		print(" ", end=" ")
		for z in range(self.width):
			print(z+1, end=" ")
		print("")
		startNum = 65
		for y in range(self.height):
			print(chr(startNum), end=" ")
			startNum = startNum + 1
			for x in range(self.width):
				print(self.grid[y][x], end=" ")
			print("")
	def change_val(self, coord, val):
		rowCol = convert_coord(coord)
		self.grid[rowCol[0]][rowCol[1]] = val
def convert_coord(coord):
	letter = coord[0:1]
	tempNum = coord[1:]
	letterConv = ord(letter)
	letterConv = letterConv - 65
	num = int(tempNum)
	num = num - 1
	return (letterConv, num)
def rev_convert_coord(y, x):
	return chr(y+65) + str(x+1)	
