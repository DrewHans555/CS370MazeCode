# This class creates a Maze object of size (totalRows, totalCols).  Each node in the maze should
# be thought of as an open space surrounded by four walls with the position (rowPosition, colPosition).

from MazeNode import MazeNode
from random import shuffle, randrange
import sys


class Maze:
    # defines constructor for Maze class
    def __init__(self, totalRows=0, totalCols=0):
        self.mazeArray = []
        self.visitedNodesIndexes = []
        self.totalRows = totalRows
        self.totalCols = totalCols

        # reset the recursion limit for large mazes to prevent crashing
        if self.totalRows * self.totalCols > sys.getrecursionlimit():
            sys.setrecursionlimit(self.totalRows * self.totalCols + 5)

        # add stackOfNodes to the mazeArray
        self.addNodes()

        # pick a random node and start building paths using recursion
        self.buildPaths(self.mazeArray[randrange(len(self.mazeArray))])

        # pick a random node in first row to start from
        self.createStart()

        # pick a random node in last row to end from
        self.createEnd()

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.mazeArray

    # defines the string that gets displayed when printing the maze object
    def __str__(self):
        text = ""
        for x in range(len(self.mazeArray)):
            text = text + self.mazeArray[x]
        return text

    # defines method for adding stackOfNodes to mazeArray list
    def addNodes(self):
        index = 0
        for x in range(self.totalRows):
            for y in range(self.totalCols):
                self.mazeArray.append(MazeNode(x, y, index))
                index = index + 1

    # defines method for building paths using a recursive depth-first-search algorithm
    def buildPaths(self, node):
        self.visitedNodesIndexes.append(node.getIndexInMazeArray())
        legalNeighborIndexes = []

        legalNeighborIndexes = self.getLegalNeighborIndexes(node)

        # if there are one or more legal neighbor stackOfNodes to explore then select one from neighborNodesIndexes
        # and destroyWallBetweenNodes then call buildPaths using the new node
        # else you've reached a dead end and should backtrack to previous node
        if not legalNeighborIndexes:
            # if there are no legal neighbor stackOfNodes then backtrack to previous node
            pass
        else:
            # if there are is one or more legal neighbor stackOfNodes to explore
            # then randomly pick one and buildPaths recursively

            # randomize list of neighborNodesIndexes to ensure random paths are generated
            shuffle(legalNeighborIndexes)

            # check every neighbor node at least once for an unvisited node to buildPaths
            for x in range(len(legalNeighborIndexes)):
                # if neighbor x has not been visited then tear down the wall between it and node
                if (legalNeighborIndexes[x] not in self.visitedNodesIndexes):
                    self.destroyWallBetweenNodes(node, self.mazeArray[legalNeighborIndexes[x]])
                    self.buildPaths(self.mazeArray[legalNeighborIndexes[x]])

    # defines method for tearing down a node wall
    def destroyWallBetweenNodes(self, node1, node2):
        # if node2 is left of node1 then destroy wall between node2 right and node1 left
        if node1.isLeftOf(node2):
            node1.setRightWalkable()
            node2.setLeftWalkable()

        # if node2 is right of node1 then destroy wall between node2 left and node1 right
        if node1.isRightOf(node2):
            node1.setLeftWalkable()
            node2.setRightWalkable()

        # if node2 is top of node1 then destroy wall between node2 bottom and node1 top
        if node1.isAboveOf(node2):
            node1.setBottomWalkable()
            node2.setTopWalkable()

        # if node2 is bottom of node1 then destroy wall between node2 top and node1 bottom
        if node1.isBelowOf(node2):
            node1.setTopWalkable()
            node2.setBottomWalkable()

    # defines method for creating a start node
    def createStart(self):
        startNodeIndex = randrange(self.totalCols)
        startNode = self.mazeArray[startNodeIndex]
        startNode.setAsMazeStart()

    # defines method for creating an end node
    def createEnd(self):
        endNodeIndex = (int(self.totalRows - 1) * int(self.totalCols)) + randrange(self.totalCols)
        endNode = self.mazeArray[endNodeIndex]
        endNode.setAsMazeEnd()

    # defines method for getting the list of mazeArray indexes of legal neighbor stackOfNodes (if those neighbors exist)
    def getLegalNeighborIndexes(self, node):
        legalNeighbors = []

        # if node's neighbor is legal, exists and isn't the previous visited node, then add it to neighborNodesIndexes
        if node.hasLeftNeighbor():
            legalNeighbors.append(node.getLeftNeighborIndex(self.totalCols))
        if node.hasRightNeighbor(self.totalCols):
            legalNeighbors.append(node.getRightNeighborIndex(self.totalCols))
        if node.hasTopNeighbor():
            legalNeighbors.append(node.getTopNeighborIndex(self.totalCols))
        if node.hasBottomNeighbor(self.totalRows):
            legalNeighbors.append(node.getBottomNeighborIndex(self.totalRows, self.totalCols))

        return legalNeighbors

    # defines method for getting the mazeArray list
    def getMazeArray(self):
        return self.mazeArray

    # defines method for getting a node's mazeArray index given it's rowPosition and colPosition
    def getNodeIndex(self, rowPos, colPos):
        # Given an M*N grid with M rows and N columns and given a grid element (R, C), where R
        # is in [0, M) and C is in [0, N), finding the element's index I in an ordered list
        # of all grid elements of M*N grid is given by I = R*N + C.
        return ((rowPos * int(self.totalCols)) + colPos)

    # defines method for getting the number of totalNodes in maze
    def getTotalNodes(self):
        return self.totalRows * self.totalCols

    # defines method for getting the number of totalRows in maze
    def getTotalRows(self):
        return self.totalRows

    # defines method for getting the number of totalCols in maze
    def getTotalCols(self):
        return self.totalCols

    # defines method for printing out a text-picture of the generated maze
    def printMazePicture(self):
        # print one row at a time
        for r in range(self.totalRows):
            # visit each node in the row 3 times
            for x in range(3):
                # for each node in the row print out 3 lines for the tops, middles, and bottoms
                for c in range(self.totalCols):
                    # recall: index for a grid item in an ordered list I = rowPos*totalCols + colPos
                    currentNode = self.mazeArray[r * self.totalCols + c]
                    if (x == 0 and currentNode.getTopWalkable() == False):
                        print("+---", end="")
                    if (x == 0 and currentNode.getTopWalkable() == True):
                        print("+   ", end="")
                    if (x == 0 and c == self.totalCols - 1):
                        print("+", end="")
                        print("")

                    if (x == 1 and currentNode.getLeftWalkable() == False):
                        print("|   ", end="")
                    if (x == 1 and currentNode.getLeftWalkable() == True):
                        print("    ", end="")
                    if (x == 1 and c == self.totalCols - 1):
                        print("|", end="")
                        print("")

                    if ((x == 2 and r == self.totalRows - 1) and currentNode.getBottomWalkable() == False):
                        print("+---", end="")
                    if ((x == 2 and r == self.totalRows - 1) and currentNode.getBottomWalkable() == True):
                        print("+   ", end="")
                    if ((x == 2 and r == self.totalRows - 1) and c == self.totalCols - 1):
                        print("+", end="")
                        print("")
