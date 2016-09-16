# This class takes in a Maze, as a list of MazeNode objects (each knowing if they are the start/ end of the maze,
# and which of their sides have walls or walkable space), and returns a solution to the maze using a path-finding
# algorithm (depth-first-search, breadth-first-search, A*, etc.).

import queue


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, mazeArray, mazeRows, mazeCols):
        self.longestSolveTime = 0.0
        self.fastestSolveTime = 0.0
        self.averageSolveTime = 0.0

        self.mazeNodes = mazeArray
        self.mazeRows = mazeRows
        self.mazeCols = mazeCols

        self.startIndex = -1
        self.endIndex = -1

        self.solutionPath = []

        for x in range(len(self.mazeNodes)):
            if self.mazeNodes[x].isStartOfMaze:
                self.startIndex = x
            if self.mazeNodes[x].isEndOfMaze:
                self.endIndex = x

    # defines representation for Python Interpreter
    def __repr__(self):
        return self

    # defines method for finding a path from the start node to the end node
    def depthFirstSearchWithStack(self):
        pass

    # defines method for finding a path from the start node to the end node
    def depthFirstSearchWithRecursion(self):
        pass

    # defines method for finding a path from the start node to the end node
    def breadthFirstSearchWithQueue(self):
        pass

    # defines method for finding a path from the start node to the end node
    def breadthFirstSearchWithRecursion(self):
        pass

    # defines method for finding a solution path with a recursive A* Algorithm
    def solveWithAStar(self):
        # priority queue that stores the cost value and index of nodes
        self.mazeNodes[self.startIndex].setFValue(0)
        pqOfOpenNodeIndexes = queue.PriorityQueue(0)
        pqOfOpenNodeIndexes.put([0, self.startIndex])
        listOfCheckedNodes = []
        solutionPath = self.aStarSearch(pqOfOpenNodeIndexes, listOfCheckedNodes)
        return solutionPath

    # defines method for finding a path from the start node to the end node
    def aStarSearch(self, openNodesPQ, checkedNodes):
        # get the node index with lowest f value in openNodesPQ
        lowestFValueIndex = openNodesPQ.get()[1]
        currentNode = self.mazeNodes[lowestFValueIndex]

        # get the legal walkable neighbor node indexes
        neighborNodeIndexes = self.getWalkableNeighborNodes(currentNode)

        # for each neighbor
        for x in range(len(neighborNodeIndexes)):
            neighborNodeIndex = neighborNodeIndexes[x]
            neighborNode = self.mazeNodes[neighborNodeIndex]

            # set the neighbor node's parent to the currentNode's index
            neighborNode.setParentIndex(currentNode.getIndexInMazeArray())

            # if end is found then stop searching and return the solution path
            if neighborNode.isEndOfMaze:
                return self.getSolutionPath(neighborNode)

            # get the neighbor node's fValue with respect to the currentNode
            fValue = self.getFValue(currentNode, neighborNode)

            # add neighborNode to openNodesPQ with it's better fValue
            if neighborNode.getFValue() == -1 or fValue < neighborNode.getFValue():
                neighborNode.setFValue(fValue)
                openNodesPQ.put([fValue, neighborNodeIndex])
            checkedNodes.append(currentNode.getIndexInMazeArray())
        self.aStarSearch(openNodesPQ, checkedNodes)


    # define method getting the indexs of legal, walkable neighbor nodes
    def getWalkableNeighborNodes(self, currentNode):
        walkableNeighbors = []
        # if node's neighbor is legal, exists and isn't the previous visited node, then add it to neighborNodesIndexes
        if currentNode.hasLeftNeighbor() and currentNode.getLeftWalkable():
            walkableNeighbors.append(currentNode.getLeftNeighborIndex(self.mazeCols))
        if currentNode.hasRightNeighbor(self.mazeCols) and currentNode.getRightWalkable():
            walkableNeighbors.append(currentNode.getRightNeighborIndex(self.mazeCols))
        if currentNode.hasTopNeighbor() and currentNode.getTopWalkable():
            walkableNeighbors.append(currentNode.getTopNeighborIndex(self.mazeCols))
        if currentNode.hasBottomNeighbor(self.mazeRows) and currentNode.getBottomWalkable():
            walkableNeighbors.append(currentNode.getBottomNeighborIndex(self.mazeRows, self.mazeCols))
        return walkableNeighbors

    # defines method for generating the total cost of moving from one node to another
    def getFValue(self, currentNode, givenNode):
        return int(self.getGValue(currentNode, givenNode) + self.getHValue(givenNode))

    # defines method for getting the cost it takes to get from current node to a given node
    def getGValue(self, currentNode, givenNode):
        # moving upwards takes you farther from the bottom row where the goalNode (so high cost)
        if givenNode.isAboveOf(currentNode):
            return 20
            # moving left or right keeps you at the same level (so moderate cost)
        if givenNode.isLeftOf(currentNode) or givenNode.isRightOf(currentNode):
            return 15
            # moving down gets you closer to the bottom row where the goalNode is (so low cost)
        if givenNode.isBelowOf(currentNode):
            return 10

    # defines method for getting the heuristic value of a given node
    def getHValue(self, givenNode):
        # given two points P(p1,p2) and Q(q1,q2), the taxicab distance D between P and Q is
        # given by the equation D = |p1-q1| + |p2-q2|
        goalNode = self.mazeNodes[self.endIndex]
        return abs(givenNode.getRowPosition() - goalNode.getRowPosition()) + abs(
            givenNode.getColPosition() - goalNode.getColPosition())

    # http://stackoverflow.com/questions/22737111/check-if-something-is-already-in-priority-queue-python
    def getSolutionPath(self, node):
        if node.getParentIndex() == -1:
            return self.solutionPath
        else:
            self.solutionPath.append(node)
            self.getSolutionPath(self.mazeNodes[node.getParentIndex()])

    #
    def printSolutionPath(self, path):
        print("Solution:  ")
        print(*path, sep='\n')

    # defines method for printing out the solve time information
    def printSolveTime(self, algorithm):
        print(algorithm + " results: ")
        print("    -longestSolveTime = " + str(self.longestSolveTime))
        print("    -fastestSolveTime = " + str(self.longestSolveTime))
        print("    -averageSolveTime = " + str(self.longestSolveTime))
