# This class takes in a Maze, as a list of MazeNode objects (each knowing if they are the start/ end of the maze,
# and which of their sides have walls or walkable space), and returns a solution to the maze using a path-finding
# algorithm (depth-first-search, breadth-first-search, A*, etc.).

from Maze import Maze


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, listOfMazeNodes):
        self.longestSolveTime = 0.0
        self.fastestSolveTime = 0.0
        self.averageSolveTime = 0.0

        startIndex = -1
        endIndex = -1

        for x in range(len(listOfMazeNodes)):
            if listOfMazeNodes[x].isStartOfMaze():
                startIndex = x
            if listOfMazeNodes[x].isEndOfMaze():
                endIndex = x

    # defines representation for Python Interpreter
    def __repr__(self):
        return self

    # defines method for finding a path from a start node to an end node
    def depthFirstSearchWithStack(self, listOfMazeNodes, indexOfStart, indexOfEnd):

        self.printSolveTime("depthFirstSearchWithStack")

    # defines method for finding a path from a start node to an end node
    def depthFirstSearchWithRecursion(self, listOfMazeNodes, indexOfStart, indexOfEnd):
        pass

    # defines method for finding a path from a start node to an end node
    def breadthFirstSearchWithQueue(self, listOfMazeNodes, indexOfStart, indexOfEnd):
        pass

    # defines method for finding a path from a start node to an end node
    def breadthFirstSearchWithRecursion(self, listOfMazeNodes, indexOfStart, indexOfEnd):
        pass
    
    #
    def printSolveTime(self, algorithmUsedToSolve):
        print(algorithmUsedToSolve + " results: ")
        print("    -longestSolveTime = " + str(self.longestSolveTime))
        print("    -fastestSolveTime = " + str(self.longestSolveTime))
        print("    -averageSolveTime = " + str(self.longestSolveTime))
