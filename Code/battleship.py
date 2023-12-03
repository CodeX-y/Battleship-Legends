
import random

board = []

for x in range(10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return random.randint(0, len(board) - 1)

def random_col(board):
  return random.randint(0, len(board[0]) - 1)

def random_orientation():
  return random.choice(["horizontal", "vertical"])

ships = [
  {"size": 2, "orientation": "horizontal", "name": "Ship 1"},
  {"size": 3, "orientation": "horizontal", "name": "Ship 2"},
  {"size": 4, "orientation": "horizontal", "name": "Ship 3"},
  {"size": 5, "orientation": "horizontal", "name": "Ship 4"}
]

for ship in ships:
  ship["row"] = random_row(board)
  ship["col"] = random_col(board)
  ship["orientation"] = random_orientation()
  if ship["orientation"] == "horizontal":
    if ship["col"] + ship["size"] > len(board[0]):
        ship["col"] = random_col(board)
  if ship["col"] + ship["size"] <= len(board[0]):
    for i in range(ship["size"]):
        board[ship["row"]][ship["col"] + i] = "X"
  elif ship["orientation"] == "vertical":
    if ship["row"] + ship["size"] > len(board):
        ship["row"] = random_row(board)
    if ship["row"] + ship["size"] <= len(board):
        for i in range(ship["size"]):
            board[ship["row"] + i][ship["col"]] = "X"


num_of_turns = int(input("Enter number of turns: "))
turn = 0
ships_left = len(ships)

while ships_left > 0 and turn < num_of_turns:
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  hit = False
  for ship in ships:
    if ship["orientation"] == "horizontal":
      if guess_row == ship["row"] and \
         guess_col >= ship["col"] and \
         guess_col < ship["col"] + ship["size"]:
        print("You hit my", ship["name"] + "!")
        for i in range(ship["size"]):
          if board[guess_row][ship["col"] + i] != "H":
            board[guess_row][ship["col"] + i] = "H"
            hit = True
        if hit:
          print("You sank a", ship["size"], "size ship!")
          ships_left -= 1
    elif ship["orientation"] == "vertical":
      if guess_col == ship["col"] and \
         guess_row >= ship["row"] and \
         guess_row < ship["row"] + ship["size"]:
        print("You hit my", ship["name"] + "!")
        board[guess_row][guess_col] = "H"
        hit = True
        ships_left -= 1

  if not hit:
    if guess_row not in range(len(board)) or \
      guess_col not in range(len(board[0])):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X" or \
         board[guess_row][guess_col] == "H":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "M"

  turn += 1

if ships_left == 0:
  print("Congratulations! You sank all my battleships!")
else:
  print("Game Over")

print_board(board)
