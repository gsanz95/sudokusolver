'''
@Author Giancarlo Sanz
@Version 1.0.0
@Name Sudoku Launcher
'''
from setup import readBoardsFromFile
from board import Board
from logger import *

# Starts the program
def startProgram():
    fileName = "puzzles.txt"
    boards = []
    boards = readBoardsFromFile(fileName, 50)
    trySolvingBoards(boards)

# Tries solving each board and prints it finished 
def trySolvingBoards(boards):
    for singleBoard in boards:
        i = 1
        while i  > 0:
            i = trySingleChoices(singleBoard)
            singleBoard.tryCompleteCols()
            singleBoard.tryCompleteRows()
            singleBoard.tryCompleteSquares()
        boardLogger.printBoardInfo(singleBoard)
        

# Iterates over all cells and
# tries to fill cell
def trySingleChoices(singleBoard):
    filledCells = 0
    for i in range(0, singleBoard.size):
        for j in range(0, singleBoard.size):
            filledCells += tryFillCell(singleBoard, i, j)

    return filledCells

# If the cell is not filled
# calls all possible values
# for the cell and when there
# is a single possible value
# the cell will be updated
# return 1 if cell value updated
def tryFillCell(singleBoard, row, col):
    if singleBoard.cells[row][col] == 0:
        possibleValues = singleBoard.generateOptions(row, col)

        if len(possibleValues) == 1:
            singleBoard.updateCell(row, col, possibleValues[0])
            #print(singleBoard)                             # Uncomment this line to board after each new cell added
            return 1
    return 0

# Start from here
boardLogger = Logger()
startProgram()