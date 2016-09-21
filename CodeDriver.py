# This class drives the PythonMazeCode classes

from Maze import Maze
from MazeSolver import MazeSolver
from time import clock
import sys


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

    #
    def runAStarTest(self, mazeRows, mazeCols, numberOfTests):
        totalNodes = mazeRows * mazeCols
        totalVisitedNodes = 0
        totalSolveTime = 0

        # reset the recursion limit for large mazes to prevent crashing
        if totalNodes > sys.getrecursionlimit():
            sys.setrecursionlimit(totalNodes + 5)

        print("Running AStar Test...")
        testStartTime = clock()  # get the time before you run all tests
        for x in range(numberOfTests):
            maze = Maze(mazeRows, mazeCols)  # create new maze object
            solver = MazeSolver(maze)  # create new solver object
            startTime = clock()  # get the time right before solving
            path = solver.solveWithAStar()  # solve the new maze with AStar
            solveTime = clock() - startTime  # get the time spent solving

            # get test x data
            visitedNodes = solver.getNodesExplored()
            totalSolveTime = totalSolveTime + solveTime
            totalVisitedNodes = totalVisitedNodes + visitedNodes

        testFinishTime = clock() - testStartTime  # get the time after you run all tests
        solveTimeAverage = totalSolveTime / numberOfTests
        spaceComplexityAverage = totalVisitedNodes / (totalNodes * numberOfTests)

        print("Finished AStar Test in  " + "{:.4E}".format(testFinishTime) + " seconds")
        print("-Total Number of Tests performed:  " + str(numberOfTests))
        print("-Average Solve Time:  " + "{:.4E}".format(solveTimeAverage) + " seconds")
        print("-Average Percent of Nodes Visited:  " + str(spaceComplexityAverage * 100) + " %")


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
# maze = driver.generateMaze(10, 20)
# driver.printMazePicture(maze)
# driver.solveMazeWithAStar(maze)
# driver.solveMazeWithDFS(maze)
# driver.solveMazeWithBFS(maze)
# driver.solveMazeWithAll(maze)
driver.runAStarTest(10, 10, 10000)
