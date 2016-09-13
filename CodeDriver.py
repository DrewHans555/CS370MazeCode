# This class generates a Maze

from Maze import Maze


class CodeDriver:
    # defines constructor for MazeGenerator class
    def __init__(self):
        self.listOfMazeNodes = []

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.listOfMazeNodes

    # defines method for getting the listOfMazeNodes 
    def getMazeNodes(self):
        return self.listOfMazeNodes

    # defines method for building a new maze
    def generateMaze(self, totalRows, totalCols):
        # get the list of MazeNodes from new
        self.listOfMazeNodes = Maze(totalRows, totalCols).printMazePicture()

    #
    def solveMaze(self):
        pass

    #
    def performMultipleTests(self, mazeRows, mazeCols, totalTests):
        for x in range(totalTests):
            self.generateMaze(mazeRows, mazeCols)
            self.solveMaze()

    #
    def outputResults(self):
        pass

CodeDriver().generateMaze(10, 10)
