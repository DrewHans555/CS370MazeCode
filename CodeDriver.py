# This class drives the PythonMazeCode classes

from Maze import Maze
from MazeSolver import MazeSolver
from time import clock


class CodeDriver:
    # defines constructor for MazeGenerator class
    def __init__(self):
        pass

    # defines representation for Python Interpreter
    def __repr__(self):
        return self

    # defines method for building a new maze object
    def generateMaze(self, totalRows, totalCols):
        mazeObject = Maze(totalRows, totalCols)
        return mazeObject

    # defines method for solving the maze with A Star Algorithm
    def solveMazeWithAStar(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithAStar()
        stopTime = clock() - startTime
        self.printSolveTime("A*", stopTime)
        solver.printSolutionPath(path)

    # defines method for printing a text picture of the maze
    def printMazePicture(self, mazeObject):
        mazeObject.printMazePicture()

    # defines method for printing the time it took to find a solution path
    def printSolveTime(self, algorithmUsed, solveTime):
        print("A solution path was found with " + algorithmUsed + " in " + "{:.2E}".format(solveTime) + " seconds")


driver = CodeDriver()
maze = driver.generateMaze(5, 5)
driver.printMazePicture(maze)
driver.solveMazeWithAStar(maze)
