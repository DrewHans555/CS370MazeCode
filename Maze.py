# This class creates a Maze object of size (totalRows, totalCols).  Each node in the maze should
# be thought of as an open space surrounded by four walls with the position (rowPosition, colPosition).

from MazeNode import MazeNode
from random import shuffle, randrange
import sys


class Maze:
    # defines constructor for Maze class
    def __init__(self, totalRows=0, totalCols=0):
        self.mazeArray = []
        self.listOfVisitedNodes = []
        self.totalRows = totalRows
        self.totalCols = totalCols

        # reset the recursion limit for large mazes
        if self.totalRows * self.totalCols > sys.getrecursionlimit():
            sys.setrecursionlimit(self.totalRows * self.totalCols + 5)

        self.addNodes()  # add nodes to the mazeArray
        self.setMazeBounds()  # set the maze boundaries

        randomNode = self.mazeArray[randrange(len(self.mazeArray))]
        self.buildPaths(randomNode)  # build paths using recursion

        self.printMazePicture()

    # defines representation for Python Interpreter
    def __repr__(self):
        return [self.mazeArray]

    # defines the string that gets displayed when printing the maze object
    def __str__(self):
        text = ""
        for x in range(len(self.mazeArray)):
            text = text + self.mazeArray[x]
        return text

    # defines method for adding nodes to mazeArray list
    def addNodes(self):
        for x in range(self.totalRows):
            for y in range(self.totalCols):
                self.mazeArray.append(MazeNode(x, y))

    # defines method for setting the maze bounds
    def setMazeBounds(self):
        for x in range(len(self.mazeArray)):
            currentNode = self.mazeArray[x]
            # if node has a side that is a boundary of the maze
            # then set that side to not be openable
            if (currentNode.rowPosition == 0):
                currentNode.setTopOpenable(False)
            if (currentNode.rowPosition == self.totalRows - 1):
                currentNode.setBottomOpenable(False)
            if (currentNode.colPosition == 0):
                currentNode.setLeftOpenable(False)
            if (currentNode.colPosition == self.totalCols - 1):
                currentNode.setRightOpenable(False)

    # defines method for building paths using a recursive depth-first-search algorithm
    def buildPaths(self, node):
        self.listOfVisitedNodes.append(node)
        neighborNodesIndex = []

        leftNeighborRowPos = node.getLeftNeighborRowPosition()
        leftNeighborColPos = node.getLeftNeighborColPosition()
        rightNeighborRowPos = node.getRightNeighborRowPosition(self.totalCols)
        rightNeighborColPos = node.getRightNeighborColPosition(self.totalCols)
        topNeighborRowPos = node.getTopNeighborRowPosition()
        topNeighborColPos = node.getTopNeighborColPosition()
        bottomNeighborRowPos = node.getBottomNeighborRowPosition(self.totalRows)
        bottomNeighborColPos = node.getBottomNeighborColPosition(self.totalRows)

        # if node's neighbor is legal then add it to neighborNodesIndex list
        if (leftNeighborRowPos is not None) and (leftNeighborColPos is not None):
            neighborNodesIndex.append(self.getNodeNeighborIndex(leftNeighborRowPos, leftNeighborColPos))
        if (rightNeighborRowPos is not None) and (rightNeighborColPos is not None):
            neighborNodesIndex.append(self.getNodeNeighborIndex(rightNeighborRowPos, rightNeighborColPos))
        if (topNeighborRowPos is not None) and (topNeighborColPos is not None):
            neighborNodesIndex.append(self.getNodeNeighborIndex(topNeighborRowPos, topNeighborColPos))
        if (bottomNeighborRowPos is not None) and (bottomNeighborColPos is not None):
            neighborNodesIndex.append(self.getNodeNeighborIndex(bottomNeighborRowPos, bottomNeighborColPos))

        # if you reach a dead end then do nothing and backtrack to previous node
        if neighborNodesIndex:
            # randomize list of neighborNodesIndex to ensure random paths are generated
            shuffle(neighborNodesIndex)

            # check every neighbor at least once
            for x in range(len(neighborNodesIndex)):
                # if neighbor x has not been visited then tear down the wall between it and node
                if (self.mazeArray[neighborNodesIndex[x]] not in self.listOfVisitedNodes):
                    self.destroyWallBetweenNodes(node, self.mazeArray[neighborNodesIndex[x]])
                    self.buildPaths(self.mazeArray[neighborNodesIndex[x]])

    # defines method for getting a node's neighbor's mazeArray index
    def getNodeNeighborIndex(self, neighborRowPos, neighborColPos):
        # Given an M*N grid with M rows and N columns and given a grid element (R, C), where R
        # is in [0, M) and C is in [0, N), finding the element's index I in an ordered list
        # of all grid elements of M*N grid is given by I = R*N + C.
        return ((neighborRowPos * int(self.totalCols)) + neighborColPos)

    # defines method for tearing down a node wall
    def destroyWallBetweenNodes(self, node1, node2):
        # if node2 is left of node1 then destroy wall between node2 right and node1 left
        if ((node2.getRowPosition() == node1.getRowPosition()) and
                (node2.getColPosition() + 1 == node1.getColPosition())):
            node1.setLeftWalkable()
            node2.setRightWalkable()

        # if node2 is right of node1 then destroy wall between node2 left and node1 right
        if ((node2.getRowPosition() == node1.getRowPosition()) and
                (node2.getColPosition() - 1 == node1.getColPosition())):
            node1.setRightWalkable()
            node2.setLeftWalkable()

        # if node2 is top of node1 then destroy wall between node2 bottom and node1 top
        if ((node2.getColPosition() == node1.getColPosition()) and
                (node2.getRowPosition() + 1 == node1.getRowPosition())):
            node1.setTopWalkable()
            node2.setBottomWalkable()

        # if node2 is bottom of node1 then destroy wall between node2 top and node1 bottom
        if ((node2.getColPosition() == node1.getColPosition()) and
                (node2.getRowPosition() - 1 == node1.getColPosition())):
            node1.setBottomWalkable()
            node2.setTopWalkable()

    # defines method for getting the mazeArray list
    def getMazeArray(self):
        return self.mazeArray

    # defines method for getting the number of totalNodes in maze
    def getTotalNodes(self):
        return self.totalRows * self.totalCols

    # defines method for getting the number of totalRows in maze
    def getTotalRows(self):
        return self.totalRows

    # defines method for getting the number of totalCols in maze
    def getTotalCols(self):
        return self.totalCols

        #

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
                        print("+--", end="")
                    if (x == 0 and currentNode.getTopWalkable() == True):
                        print("+  ", end="")
                    if (x == 0 and c == self.totalCols - 1):
                        print("+", end="")
                        print("")

                    if (x == 1 and currentNode.getLeftWalkable() == False):
                        print("|  ", end="")
                    if (x == 1 and currentNode.getLeftWalkable() == True):
                        print("   ", end="")
                    if (x == 1 and c == self.totalCols - 1):
                        print("|", end="")
                        print("")

                    if (x == 2 and r == self.totalRows - 1):
                        print("+--", end="")
                        if (x == 2 and c == self.totalCols - 1):
                            print("+", end="")
                            print("")
