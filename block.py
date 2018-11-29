import math

class Block:
    def __init__(self, cellNumber ,cellsToSet):
        size = int(len(cellsToSet))
        self.cells = []

        # Save cells within cellNumber
        for row in range(0, size):
            for col in range(0, size):
                self.cells.append(cellsToSet[row][(size * cellNumber) + col])

    def __str__(self):
        return '{}\n{}\n{}\n'.format(self.cells[0:3], self.cells[3:6], self.cells[6:9])

    # Get row of this block
    def getRow(self, rowToGet):
        dimension = int(math.sqrt(len(self.cells)))
        return self.cells[(rowToGet*dimension):(rowToGet*dimension) + dimension]

    # Get column of this block
    def getCol(self, colToGet):
        cellHolder = []
        dimension = int(math.sqrt(len(self.cells)))
        for i in range(0, dimension):
            cellHolder.append(self.cells[(dimension*i)+colToGet])

        return cellHolder

    #def tryCompleteBlock(self):