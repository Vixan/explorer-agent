from defs import CELL_PROP

class Board:
    __grid = []

    def __init__(self, grid):
        self.__grid = grid

    def getGrid(self):
        return self.__grid

    def drawGrid(self):
        path = self.__grid
        
        for x in range(0, len(path)):
            for y in range(0, len(path[x])):
                if (path[x][y] == CELL_PROP["VISITED"]):
                    print("*", end=" ")
                elif (path[x][y] == CELL_PROP["BLOCKED"]):
                    print("#", end=" ")
                elif (path[x][y] == CELL_PROP["DANGEROUS"]):
                    print("M", end=" ")
                elif (path[x][y] == CELL_PROP["LUCKY"]):
                    print("T", end=" ")
                else:
                    print('_', end=" ")
            print()

    def getCell(self, row, col):
        return self.__grid[row][col]

    def setCellVisited(self, row, col):
        self.__grid[row][col] = CELL_PROP["VISITED"]
    
    def setCellEmpty(self, row, col):
        self.__grid[row][col] = CELL_PROP["EMPTY"]

    def setCellDangerous(self, row, col):
        self.__grid[row][col] = CELL_PROP["DANGEROUS"]
        