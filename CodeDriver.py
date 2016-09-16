# This class drives the PythonMazeCode classes

from Maze import Maze
from MazeSolver import MazeSolver


class CodeDriver:
    # defines constructor for MazeGenerator class
    def __init__(self):
        self.listOfMazeNodes = []
        self.mazeRows = -1
        self.mazeCols = -1

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.listOfMazeNodes

    # defines method for getting the listOfMazeNodes 
    def getMazeNodes(self):
        return self.listOfMazeNodes

    # defines method for getting the number of maze rows after generateMaze is called
    def getMazeRows(self):
        return self.mazeRows

    # defines method for getting the number of maze cols after generateMaze is called
    def getMazeCols(self):
        return self.mazeCols

    # defines method for building a new maze
    def generateMaze(self, totalRows, totalCols):
        # get the list of MazeNodes from new
        maze = Maze(totalRows, totalCols)
        maze.printMazePicture()
        self.listOfMazeNodes = maze.getMazeArray()

    #
    def solveMaze(self):
        solver = MazeSolver(self.listOfMazeNodes, self.mazeRows, self.mazeCols)
        path = solver.solveWithAStar()
        solver.printSolutionPath(path)


    #
    def performMultipleTests(self, mazeRows, mazeCols, totalTests):
        for x in range(totalTests):
            self.generateMaze(mazeRows, mazeCols)
            self.solveMaze()


driver = CodeDriver()
driver.generateMaze(10, 15)
driver.solveMaze()
