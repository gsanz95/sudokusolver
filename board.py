import copy
import math
from misc import *
#from block import Block

class Board:
    
    # Creates board and saves ID and difficulty
    # and initiates a list for the cells.
    def __init__(self, boardId, difficulty = "NORMAL"):
        self.id = boardId
        self.difficulty = difficulty
        self.cells = []
        self.cellPossibilities = dict()

    # Deep copies the list passed
    def setCells(self, cellsToSet):
        self.cells = copy.deepcopy(cellsToSet)
        self.size = int(len(self.cells))

    # To string
    def __str__(self):
        outputText = ""
        for row in range(0, self.size):
            for col in range(0, self.size):
                outputText += str(self.cells[row][col])
                outputText += " "
            outputText += "\n"
        return outputText

    # Returns a list containing values in row
    # number passed
    def getRow(self, rowNumber):
        rowHolder = []
        for col in range(0, self.size):
            rowHolder.append(self.cells[rowNumber][col])
        return rowHolder

    # Returns a list containing values in column
    # number passed
    def getCol(self, colNumber):
        colHolder = []
        for row in range(0, self.size):
            colHolder.append(self.cells[row][colNumber])
        return colHolder

    # Returns a list containing values in
    # a square determined by the number passed
    def getSquare(self, rowNumber, colNumber):
        cellHolder = []
        squareSize = int(math.sqrt(self.size))

        # Start top-left most square
        while rowNumber%squareSize != 0:
            rowNumber -= 1

        while colNumber%squareSize != 0:
            colNumber -= 1    

        # Gather square cells
        for i in range(0, squareSize):
            for j in range(0, squareSize):
                cellHolder.append(self.cells[rowNumber+i][colNumber+j])

        return cellHolder

    # Looks if any rows have a single empty
    # cell and fills it with the missing number
    def tryCompleteRows(self):
        for rowNumber in range(0, self.size):
            row = self.getRow(rowNumber)

            # No empty cells
            if 0 not in row:
                continue

            # Single empty cell
            if(hasUniqueNumbers(row)):
                colNumber = row.index(0)
                valueForCell = findMissingNumber(row)
                self.cells[rowNumber][colNumber] = valueForCell

    # Looks if any columns have a single empty
    # cell and fills it with the missing number
    def tryCompleteCols(self):
        for colNumber in range(0, self.size):
            col = self.getCol(colNumber)

            # No empty cells
            if 0 not in col:
                continue
            
            # Single empty cell
            if(hasUniqueNumbers(col)):
                rowNumber = col.index(0)
                valueForCell = findMissingNumber(col)
                self.cells[rowNumber][colNumber] = valueForCell

    # Looks if any squares have a single empty
    # cell and tries to fill them
    def tryCompleteSquares(self):
        for row in range(0, self.size, int(math.sqrt(self.size))):
            for col in range(0, self.size, int(math.sqrt(self.size))):
                square = self.getSquare(row, col)

                # Single empty cell
                if(hasUniqueNumbers(square)):
                    valueForCell = findMissingNumber(square)
                    self.completeSquare(row, col, valueForCell)

    # Fills square referenced by passed value
    # with the new value passed
    def completeSquare(self, rowNumber, colNumber, newValue):
        squareSize = int(math.sqrt(self.size))
        # Start top-left most square
        while rowNumber%squareSize != 0:
            rowNumber -= 1

        while colNumber%squareSize != 0:
            colNumber -= 1

        # Gather square cells
        for i in range(0, squareSize):
            for j in range(0, squareSize):
                if self.cells[rowNumber+i][colNumber+j] == 0:
                    self.updateCell(rowNumber+i,colNumber+j, newValue)

    # Updates a cell's value located
    # at rowNumber and colNumber
    def updateCell(self, rowNumber, colNumber, newValue):
        self.cells[rowNumber][colNumber] = newValue

    # Collects possible values that the cell at
    # rowNumber and colNumber can hold
    def generateOptions(self, rowNumber, colNumber):
        # Generate all possible values
        possibleVals = [x for x in range(1, self.size+1)]
        
        # Get cells already filled
        rowVals = self.getRow(rowNumber)
        colVals = self.getCol(colNumber)
        sqrVals = self.getSquare(rowNumber, colNumber)

        # Substract those values from the list of values
        possibleVals = [value for value in possibleVals if value not in rowVals]
        possibleVals = [value for value in possibleVals if value not in colVals]
        possibleVals = [value for value in possibleVals if value not in sqrVals]

        return possibleVals