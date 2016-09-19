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

    # defines method for solving the maze with depth-first search algorithm
    def solveMazeWithDFS(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithDFS()
        stopTime = clock() - startTime
        self.printSolveTime("Depth-First Search", stopTime)
        self.printSolutionPath(path)

    # defines method for solving the maze with breadth-first search algorithm
    def solveMazeWithBFS(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithBFS()
        stopTime = clock() - startTime
        self.printSolveTime("Breadth-First Search", stopTime)
        self.printSolutionPath(path)

    # defines method for solving the maze with A Star Algorithm
    def solveMazeWithAStar(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithAStar()
        stopTime = clock() - startTime
        self.printSolveTime("A*", stopTime)
        self.printSolutionPath(path)

    # defines method for solving the maze with all algorithms once
    def solveMazeWithAll(self, mazeObject):
        dfsSolver = MazeSolver(mazeObject)
        bfsSolver = MazeSolver(mazeObject)
        aStarSolver = MazeSolver(mazeObject)

        dfsstartTime = clock()
        dfsPath = dfsSolver.solveWithDFS()
        dfsstopTime = clock() - dfsstartTime
        self.printSolveTime("Depth-First Search", dfsstopTime)
        self.printSolutionPath(dfsPath)

        bfsstartTime = clock()
        bfsPath = bfsSolver.solveWithBFS()
        bfsstopTime = clock() - bfsstartTime
        self.printSolveTime("Breadth-First Search", bfsstopTime)
        self.printSolutionPath(bfsPath)

        # solve with A*, printSolveTime
        astarstartTime = clock()
        aStarPath = aStarSolver.solveWithAStar()
        astarstopTime = clock() - astarstartTime
        self.printSolveTime("A*", astarstopTime)
        self.printSolutionPath(aStarPath)

    # defines method for printing a text picture of the maze
    def printMazePicture(self, mazeObject):
        mazeObject.printMazePicture()

    # defines method for printing out the solution path
    def printSolutionPath(self, path):
        printCount = 0
        print("Solution Path from StartNode to EndNode:  ")
        for x in range(len(path)):
            print(path[x], end="")
            printCount = printCount + 1
            if printCount == 10:
                print("")
                printCount = 0
        print("")

    # defines method for printing the time it took to find a solution path
    def printSolveTime(self, algorithmUsed, solveTime):
        print("")
        print("A solution path was found with " + algorithmUsed + " in " + "{:.2E}".format(solveTime) + " seconds")


driver = CodeDriver()
maze = driver.generateMaze(10, 10)
driver.printMazePicture(maze)
# driver.solveMazeWithAStar(maze)
# driver.solveMazeWithDFS(maze)
# driver.solveMazeWithBFS(maze)
driver.solveMazeWithAll(maze)
