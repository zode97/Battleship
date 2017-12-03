from random import randint

board=[]

score = "0:0"


print "Hey! welcome to the Buttleship game! Let's play this game as good old times with modern futures." 
error = True
def start():
  for i in range(100):
    info = raw_input("Do you need more information about this game? (Yes/No)")
    if info == "Yes" or info == "yes" or info == "y" or info == "Y" or info == "Yep" or info == "No" or info == "no" or info =="n" or info == "N":
      break
    else:
      print "Oh! I'm sorry. I didn't catch it. Try it again"

  if info == "Yes" or info == "yes" or info == "y" or info == "Y" or info == "Yep":
    print "You will have a 10 by 10 board where you will place 10 ships with differnt sizes."
    print "Description of the ships:"
    print "Amount     Name        Size"
    print "2          Battledhip  4"
    print "3          Cruiser     3"
    print "4          Submarine   3"
    print "5          Destroyer   2"

  elif info == "No" or info == "no" or info =="n" or info == "N":
    print "Great let's start with the game!"
  
  else:
   print "Oh! I'm sorry. I didn't catch it."
start()


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


for x in range(0, 10):
      board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)


turn = 0
ships = 0
while ships<5 and turn<3:
  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)
  ship_row = random_row(board)
  ship_col = random_col(board)
  print ship_row
  print ship_col
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"    
    ships += 1
    print "You sank %s ships out of 5" % (ships)
    if ships == 5:
      print "You won!"
  else:
    if guess_row not in range(10) or \
    guess_col not in range(10):
      turn+=1
      print "Turn:", turn
      print " That's not even an ocean."
    elif board[guess_row][guess_col] == "X":
      turn+=1
      print "Turn:", turn
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      turn+=1
      print "Turn:", turn
  if (turn == 3):
    print "Game Over"
    print_board(board)
