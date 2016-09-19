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
        self.printNodesExplored("Depth-First Search", solver.getNodesExplored())
        self.printSolutionPath(path)

    # defines method for solving the maze with breadth-first search algorithm
    def solveMazeWithBFS(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithBFS()
        stopTime = clock() - startTime
        self.printSolveTime("Breadth-First Search", stopTime)
        self.printNodesExplored("Breadth-First Search", solver.getNodesExplored())
        self.printSolutionPath(path)

    # defines method for solving the maze with A Star Algorithm
    def solveMazeWithAStar(self, mazeObject):
        solver = MazeSolver(mazeObject)
        startTime = clock()
        path = solver.solveWithAStar()
        stopTime = clock() - startTime
        self.printSolveTime("A*", stopTime)
        self.printNodesExplored("A*", solver.getNodesExplored())
        self.printSolutionPath(path)

    # defines method for solving the maze with all algorithms once
    def solveMazeWithAll(self, mazeObject):
        dfsSolver = MazeSolver(mazeObject)
        bfsSolver = MazeSolver(mazeObject)
        aStarSolver = MazeSolver(mazeObject)

        dfsStartTime = clock()
        dfsPath = dfsSolver.solveWithDFS()
        dfsStopTime = clock() - dfsStartTime
        self.printSolveTime("Depth-First Search", dfsStopTime)
        self.printNodesExplored("Depth-First Search", dfsSolver.getNodesExplored())
        self.printSolutionPath(dfsPath)

        bfsStartTime = clock()
        bfsPath = bfsSolver.solveWithBFS()
        bfsStopTime = clock() - bfsStartTime
        self.printSolveTime("Breadth-First Search", bfsStopTime)
        self.printNodesExplored("Breadth-First Search", bfsSolver.getNodesExplored())
        self.printSolutionPath(bfsPath)

        # solve with A*, printSolveTime
        astarStartTime = clock()
        aStarPath = aStarSolver.solveWithAStar()
        astarStopTime = clock() - astarStartTime
        self.printSolveTime("A*", astarStopTime)
        self.printNodesExplored("A*", aStarSolver.getNodesExplored())
        self.printSolutionPath(aStarPath)

    # defines method for printing a text picture of the maze
    def printMazePicture(self, mazeObject):
        mazeObject.printMazePicture()

    # defines method for printing a text picture of the maze
    def printNodesExplored(self, algorithmUsed, value):
        print(algorithmUsed + " explored " + str(value) + " distinct nodes")

    # defines method for printing out the solution path
    def printSolutionPath(self, path):
        printCount = 0
        print("Path found:  ")
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
        print(algorithmUsed + " solved in " + "{:.2E}".format(solveTime) + " seconds")


driver = CodeDriver()
maze = driver.generateMaze(10, 20)
driver.printMazePicture(maze)
# driver.solveMazeWithAStar(maze)
# driver.solveMazeWithDFS(maze)
# driver.solveMazeWithBFS(maze)
driver.solveMazeWithAll(maze)
