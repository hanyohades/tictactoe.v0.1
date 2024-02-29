import os

winner = None
gameStart = True
userNow = ""
SIZE = 3

possibleNums = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]

userOne = input("You are X or O: ")
userTwo = ""
if userOne == "X" or userOne == "x":
	userNow = "X"
else:
	userNow = "O"

def printGameBoard(o):
	os.system("cls|| clear")
	for i in range(SIZE):
		print("\n|===|===|===|")
		print("|", end="")
		for j in range(SIZE):
			print("", gameBoard[i][j], end=" |")
	print("\n|===|===|===|")

def userInput():
	inp = int(input("Choose your move 1-9: "))
	while inp not in possibleNums:
		inp = int(input("Enter valid number: "))
	if inp == 1:
		gameBoard[0][0] = userNow
		possibleNums.remove(inp)

	elif inp == 2:
		gameBoard[0][1] = userNow
		possibleNums.remove(inp)

	elif inp == 3:
		gameBoard[0][2] = userNow
		possibleNums.remove(inp)

	elif inp == 4:
		gameBoard[1][0] = userNow
		possibleNums.remove(inp)

	elif inp == 5:
		gameBoard[1][1] = userNow
		possibleNums.remove(inp)

	elif inp == 6:
		gameBoard[1][2] = userNow
		possibleNums.remove(inp)

	elif inp == 7:
		gameBoard[2][0] = userNow
		possibleNums.remove(inp)

	elif inp == 8:
		gameBoard[2][1] = userNow
		possibleNums.remove(inp)

	elif inp == 9:
		gameBoard[2][2] = userNow
		possibleNums.remove(inp)


def switchPlayer():
	global userNow
	if userNow == "X":
		userNow = "O"
	else:
		userNow = "X"

def checkWinner(gameBoard):
	global gameStart
	for i in range(SIZE):
		if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2]:
			gameStart = False
		if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i]:
			gameStart = False
	if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
		gameStart = False
	if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
		gameStart = False
	if not possibleNums:
		printGameBoard(gameBoard)
		print("\nTie!")
		gameStart = False
	elif not gameStart:
		printGameBoard(gameBoard)
		print("\nThe winner is: " + ("O" if userNow == "X" else "X"))


while gameStart:
	printGameBoard(gameBoard)
	print("You are: "+ userNow)
	userInput()
	switchPlayer()
	checkWinner(gameBoard)