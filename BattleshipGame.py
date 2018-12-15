from random import randint

board = []

for x in range(0, 5):
	board.append(["O"] * 5)

def print_board(board):
	for row in board:
    	print " ".join(row)

print_board(board)

def random_row(board_in): 
  	return randint(0,4)

def random_col(board_in): 
  	return randint(0,4)

#randomly creates a row and column for the hidden ship by calling the two functions random_row and random_col
ship_row = random_row(board)
ship_col = random_col(board)

#allow the user to take 4 turns 
for turn in range(4):
# Asks the user to guess where the ship is located
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
# if user guesses correctly tell them congratulations and end the game
    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sunk my battleship!"
      break
    else:
	#if the user guess outside the range of the board, tell them and ask them to guess again. OR if the user guesses the same
	#answer as they already guess, tell them.
      if (guess_row < 0 or guess_row > 4) or (guess_col <        0 or guess_col > 4):
          print "Oops, that's not even in the ocean."
      elif(board[guess_row][guess_col] == "X"):
          print "You guessed that one already."    
      else:
          print "You missed my battleship!"
          board[guess_row][guess_col] = "X"
      	  if turn == 3:
              print ("Game Over")
          print (turn + 1)
      print_board(board)