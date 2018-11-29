from board import Board
import re
# Reads and returns 
def readBoardsFromFile(fileName, numberOfBoards):
    fileToRead = open(fileName,'r+')
    cellHolder = []
    boards = []
    
    # Read next board in file
    for lineRead in fileToRead:
        if len(boards) >= numberOfBoards:
            break
        lineTokens = lineRead.split()
        matchResult = re.search(r'^Grid (\d+) ?([A-z]*)$', lineRead)

        # Input and format is correct
        if matchResult != None:
            if not matchResult.group(2):
                boardHolder = Board(matchResult.group(1))
            else:
                boardHolder = Board(matchResult.group(1), matchResult.group(2))
        else:
            for token in lineTokens:
                cellHolder.append([int(c) for c in token])

        # Reached line count for a 9x9 sudoku
        if(len(cellHolder) == 9):
            boardHolder.setCells(cellHolder)
            boards.append(boardHolder)
            cellHolder.clear()
            continue

    return boards