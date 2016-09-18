# This class takes in a Maze, as a list of MazeNode objects (each knowing if they are the start/ end of the maze,
# and which of their sides have walls or walkable space), and returns a solution to the maze using a path-finding
# algorithm (depth-first-search, breadth-first-search, A*, etc.).

import queue


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, mazeObject):
        self.mazeNodes = mazeObject.getMazeArray()
        self.mazeRows = mazeObject.getTotalRows()
        self.mazeCols = mazeObject.getTotalCols()
        self.startIndex = mazeObject.getStartNodeIndex()
        self.endIndex = mazeObject.getEndNodeIndex()

        self.solutionPath = []

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
        openNodePQ = queue.PriorityQueue(0)
        self.mazeNodes[self.startIndex].setFValue(0)
        self.mazeNodes[self.startIndex].setGValue(0)
        self.mazeNodes[self.startIndex].setHValue(0)
        openNodePQ.put([0, self.startIndex])
        checkedNodes = []

        self.aStarSearch(openNodePQ, checkedNodes)

        return self.solutionPath

    # defines method for finding a path from the start node to the end node
    def aStarSearch(self, openNodesPQ, checkedNodes):
        # get the node index with lowest f value in openNodesPQ
        lowestFValueIndex = openNodesPQ.get()[1]
        currentNode = self.mazeNodes[lowestFValueIndex]

        # get the legal walkable neighbor node indexes
        neighborNodeIndexes = self.getWalkableNeighborNodes(currentNode)

        # if there are walkable neighbor nodes to explore
        if neighborNodeIndexes:
            # for each neighbor node
            for x in range(len(neighborNodeIndexes)):
                neighborNodeIndex = neighborNodeIndexes[x]
                neighborNode = self.mazeNodes[neighborNodeIndex]

                # if end is found then stop searching and return the solution path
                if neighborNode.isMazeEnd():
                    neighborNode.setParentIndex(currentNode.getIndexInMazeArray())
                    return self.getSolutionPath(neighborNode)

                if neighborNodeIndex not in checkedNodes and self.is_not_in_queue(neighborNodeIndex, openNodesPQ):
                    # set the neighbor node's parent to the currentNode's index
                    neighborNode.setParentIndex(currentNode.getIndexInMazeArray())

                    # set the neighbor node's fValue, gValue, and hValue
                    gValue = self.calculateGValue(currentNode, neighborNode)
                    hValue = self.calculateHValue(currentNode)
                    fValue = gValue + hValue
                    neighborNode.setGValue(gValue)
                    neighborNode.setHValue(hValue)
                    neighborNode.setFValue(fValue)

                    # when finished add it to the priority queue then go to next neighbor
                    openNodesPQ.put([fValue, neighborNodeIndex])
                if neighborNodeIndex not in checkedNodes and self.is_in_queue(neighborNodeIndex, openNodesPQ):
                    # check to see if this new path to the neighborNode is better than previous path
                    newGValue = self.calculateGValue(currentNode, neighborNode)
                    if newGValue < neighborNode.getGValue():
                        # set the neighbor node's parent to the currentNode's index
                        neighborNode.setParentIndex(currentNode.getIndexInMazeArray())

                        # set the neighbor node's fValue, gValue, and hValue
                        newFValue = newGValue + neighborNode.getHValue()
                        neighborNode.setGValue(newGValue)
                        neighborNode.setFValue(newFValue)

                        # when finished add it to the priority queue then go to next neighbor
                        openNodesPQ.put([newFValue, neighborNodeIndex])
            # add current node to checkedNodes after exploring all neighbors
            checkedNodes.append(currentNode.getIndexInMazeArray())
            # use recursion to do the next lowest fValue node in openNodesPQ
            self.aStarSearch(openNodesPQ, checkedNodes)

    # define method getting the indexs of legal, walkable neighbor nodes
    def getWalkableNeighborNodes(self, currentNode):
        walkableNeighbors = []

        # if node's neighbor is legal, exists and isn't the previous visited node, then add it to neighborNodesIndexes
        if (currentNode.hasLeftNeighbor()) and (currentNode.getLeftWalkable()):
            walkableNeighbors.append(currentNode.getLeftNeighborIndex(self.mazeCols))

        if (currentNode.hasRightNeighbor(self.mazeCols)) and (currentNode.getRightWalkable()):
            walkableNeighbors.append(currentNode.getRightNeighborIndex(self.mazeCols))

        if (currentNode.hasTopNeighbor()) and (currentNode.getTopWalkable()):
            walkableNeighbors.append(currentNode.getTopNeighborIndex(self.mazeCols))

        if (currentNode.hasBottomNeighbor(self.mazeRows)) and (currentNode.getBottomWalkable()):
            walkableNeighbors.append(currentNode.getBottomNeighborIndex(self.mazeRows, self.mazeCols))
        return walkableNeighbors

    # defines method for getting the cost it takes to get from current node to a given node
    def calculateGValue(self, node, givenNode):
        gValueOfThisNode = node.getGValue()
        if givenNode.isAboveOf(node):
            # moving upwards takes you farther from the bottom row where the goalNode (so higher cost)
            return gValueOfThisNode + 20
        elif givenNode.isLeftOf(node) or givenNode.isRightOf(node):
            # moving left or right keeps you at the same level (so moderate cost)
            return gValueOfThisNode + 15
        elif givenNode.isBelowOf(node):
            # moving down gets you closer to the bottom row where the goalNode is (so lower cost)
            return gValueOfThisNode + 10
        else:
            return -1

    # defines method for getting the heuristic value of a node
    def calculateHValue(self, node):
        # given two points P(p1,p2) and Q(q1,q2), the taxicab distance D between P and Q is
        # given by the equation D = |p1-q1| + |p2-q2|
        goalNode = self.mazeNodes[self.endIndex]
        return abs(node.getRowPosition() - goalNode.getRowPosition()) + abs(
            node.getColPosition() - goalNode.getColPosition())

    # http://stackoverflow.com/questions/22737111/check-if-something-is-already-in-priority-queue-python
    def getSolutionPath(self, node):
        # add node path from end to start
        string = "(" + str(node.getRowPosition()) + "," + str(node.getColPosition()) + ")"
        self.solutionPath.append(string)

        if node.getParentIndex() == -1:
            # reverse the list so that it prints the path from start node to end node
            self.solutionPath.reverse()
            return self.solutionPath
        else:
            self.getSolutionPath(self.mazeNodes[node.getParentIndex()])

    # defines method for knowing if x is in a q
    def is_in_queue(self, x, q):
        with q.mutex:
            return x in q.queue

    # defines method for knowing if x is not in a q
    def is_not_in_queue(self, x, q):
        with q.mutex:
            return not (x in q.queue)

    # defines method for printing out the solution path
    def printSolutionPath(self, path):
        printCount = 0
        print("Solution:  ")
        for x in range(len(path)):
            print(path[x], end="")
            printCount = printCount + 1
            if printCount == 10:
                print("")
                printCount = 0
