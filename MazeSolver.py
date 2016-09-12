# This class generates a Maze

from Maze import Maze


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, mazeRows, mazeCols):
        self.listOfMazeNodes = []
        self.generateMaze(mazeRows, mazeCols)
        self.printMazeNodes()

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.listOfMazeNodes

    # defines method for building a new maze
    def generateMaze(self, totalRows, totalCols):
        # get the list of MazeNodes from new
        self.listOfMazeNodes = Maze(totalRows, totalCols).getMazeArray()

    #
    def printMazeNodes(self):
        print(self.listOfMazeNodes)
        print(self.listOfMazeNodes[10].getLeftWalkable())
        print(self.listOfMazeNodes[10].getRightWalkable())
        print(self.listOfMazeNodes[10].getTopWalkable())
        print(self.listOfMazeNodes[10].getBottomWalkable())


MazeSolver(25, 25)
