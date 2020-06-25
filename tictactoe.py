"""
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
X first then O player
"""
print("The rules are simple.  Let's play Tic Tac Toe.  X is player 1.  O is player 2")
print("Type in the numbers to place your piece on that part of the board.")
row1 = ["7", "8", "9"]
row2 = ["4", "5", "6"]
row3 = ["1", "2", "3"]
print(row1)
print(row2)
print(row3)
print("Type in start() to start the game. It really is that simple.")

def increment_turns(turns):
	"""
	Increments the turns. 
	"""
	turns += 1
	return turns

def user_choice():
	"""
	Asks a player to make valid choice. 
	"""
	move = input()
	while not move.isdigit() or int(move) < 1 or int(move) > 9:
		print("Try entering a digit between 1 and 9")
		move = input()
	return int(move)

def check_vert(i, j, board, visited):
	"""
	"""
	piece = board[i][j]
	queue = [(i, j)]
	while queue:
		i, j = queue.pop()
		if board[i][j] != piece:
			return False
		visited[i][j] = True
		if i > 0 and not visited[i - 1][j]:
			queue.append((i - 1, j))
		if i < 2 and not visited[i + 1][j]:
			queue.append((i + 1, j))
	return True

def check_hor(i, j, board, visited):
	piece = board[i][j]
	queue = [(i, j)]
	while queue:
		i, j = queue.pop()
		if board[i][j] != piece:
			return False
		visited[i][j] = True
		if j > 0 and not visited[i][j - 1]:
			queue.append((i, j - 1))
		if j < 2 and not visited[i][j + 1]:
			queue.append((i, j + 1))
	return True

def check_main_diag(i, j, board, visited):
	"""
	The diagonal from (0, 0) to (2, 2)
	"""
	piece = board[i][j]
	queue = [(i, j)]
	while queue:
		i, j = queue.pop()
		if board[i][j] != piece:
			return False
		visited[i][j] = True
		if i > 0 and j > 0 and not visited[i - 1][j - 1]:
			queue.append((i - 1, j - 1))
		if i < 2 and j < 2 and not visited[i + 1][j + 1]:
			queue.append((i + 1, j + 1))
	return True

def check_sec_diag(i, j, board, visited):
	"""
	The diagonal from (0, 2) to (2, 0)
	"""
	piece = board[i][j]
	queue = [(i, j)]
	while queue:
		i, j = queue.pop()
		if board[i][j] != piece:
			return False
		visited[i][j] = True
		if i < 2 and not visited[i + 1][j - 1]:
			queue.append((i + 1, j - 1))
		if i > 0 and not visited[i - 1][j - 1]:
			queue.append((i - 1, j - 1))
	return False

def check_winner(i, j, board):
	visited = [[False]*3 for _ in range(3)]
	winner = check_vert(i, j, board, visited)
	if not winner:
		winner = check_hor(i, j, board, visited)
	if not winner and i == j:
		winner = check_main_diag(i, j, board, visited)
	if not winner and (i < j - 1 or i > j + 1 or i == j):
		winner = check_sec_diag(i, j, board, visited)
	return winner

def game(turn, board, moves, turns):
	"""
	Runs the game
	"""
	move = user_choice()
	i, j = moves[move]
	while board[i][j] != " ":
		print("You can't go there")
		move = user_choice()
		i, j = moves[move]
	if turn == 1:
		board[i][j] = "X"
		turns = increment_turns(turns)
	else:
		board[i][j] = "O"
		turns = increment_turns(turns)
	winner = check_winner(i, j, board)
	if winner:
		winner = turn
	return board, turns, winner


def printBoard(row1, row2, row3):
	map1 = ["7", "8", "9"]
	map2 = ["4", "5", "6"]
	map3 = ["1", "2", "3"]
	print(row1, map1)
	print(row2, map2)
	print(row3, map3)

def start():
	moveMap = {}
	index = 1
	for i in range(2, -1, -1):
		for j in range(3):
			moveMap[index] = (i, j)
			index += 1
	row1 = [" "]*3
	row2 = [" "]*3
	row3 = [" "]*3
	printBoard(row1, row2, row3)
	board = [row1, row2, row3]
	winner = None
	turns = 0
	turn = 1
	while not winner and turns < 9:
		board, turns, winner = game(turn, board, moveMap, turns)
		printBoard(board[0], board[1], board[2])
		turn = 2 if turn == 1 else 1
	if not winner:
		print("It is a draw!")
	else:
		print(f"Player {winner} is the winner!")






"""

1) We need a way for a player to place an X or an O.
2) Representation of the board
3) I need to keep track of if there is an X or an O at a place on the board.  
4) print the board
5) 
6) represent x as 0, and O as 1 and empty as -1

1) We need to add a feature where you can only add an X or O on empty strings.  
2) To have logic that notices a winner.  
3) user feedback to your inputs 

4) I need to add the logic for winning now.  

1) How can you win? 
2) 3 of the same characters adjacent either vertically, horizontally, or diagonally
3) check if someone has won after each player makes a move. 
4) I'm thinking of doing a dfs search from the most recent move.  And going vertically, horizontally and diagonally. 
To see if there are three in a row or column or diagonally.  

[[-1,-1,-1],
[-1,-1,-1],
[-1,-1,-1]]

_ _ _
_ _ _
_ _ _

X|_|O
_|_|_
_|_|_

"""
