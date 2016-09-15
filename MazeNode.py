# This class creates a Maze Node object that knows it's row position in the maze, column position in the maze,
# it's index in the maze array, which of it's four walls are opened and closed, and whether it is the start of
# the maze or the end of the maze or neither. Each Maze Node should be thought of as an open space surrounded
# by four walls with it's position being (rowPosition, colPosition) in a maze of size (totalRows, totalCols)
# and it's index in the maze array being equal to (rowPosition * totalCols + colPosition).
#                         +--+
#  node representation =  |  |  where -- and | represent walls and spaces are walkable space
#                         +--+
# Note:  if sideWalkable = False then a wall exists on that side
#    and if sideWalkable = True then no wall exists on that side


class MazeNode:
    # defines constructor for MazeNode class
    def __init__(self, rowPos=0, colPos=0, index=-1):
        self.isStartOfMaze = False
        self.isEndOfMaze = False

        self.rowPosition = rowPos
        self.colPosition = colPos
        self.indexInMazeArray = index

        # walkable = False means that a wall exists between stackOfNodes
        self.leftWalkable = False
        self.rightWalkable = False
        self.topWalkable = False
        self.bottomWalkable = False

        # fValue is used when solving with A*
        self.fValue = -1

        # parentIndex is used when solving with A*
        self.parentIndex = -1

    # defines representation for Python Interpreter
    def __repr__(self):
        return repr([self.rowPosition, self.colPosition])

    # defines the string that gets displayed when printing the node
    def __str__(self):
        return "(" + str(self.rowPosition) + "," + str(self.colPosition) + ")"

    # defines the method for getting the node's index in the mazeArray
    def getIndexInMazeArray(self):
        return self.indexInMazeArray

    # defines the method for getting the node's row position
    def getRowPosition(self):
        return int(self.rowPosition)

    # defines the method for getting the node's column position
    def getColPosition(self):
        return int(self.colPosition)

    # defines method for getting position of MazeNode's left neighbor's index in the mazeArray
    def getLeftNeighborIndex(self, totalMazeCols):
        if self.hasLeftNeighbor():
            return (self.rowPosition * int(totalMazeCols)) + (self.colPosition - 1)
        else:
            return -1

    # defines method for getting position of MazeNode's left neighbor's index in the mazeArray
    def getTopNeighborIndex(self, totalMazeCols):
        if self.hasTopNeighbor():
            return ((self.rowPosition - 1) * int(totalMazeCols)) + self.colPosition
        else:
            return -1

    # defines method for getting position of MazeNode's left neighbor's index in the mazeArray
    def getRightNeighborIndex(self, totalMazeCols):
        if self.hasRightNeighbor(totalMazeCols):
            return (self.rowPosition * int(totalMazeCols)) + (self.colPosition + 1)
        else:
            return -1

            # defines method for getting position of MazeNode's left neighbor's index in the mazeArray

    def getBottomNeighborIndex(self, totalMazeRows, totalMazeCols):
        if self.hasBottomNeighbor(totalMazeRows):
            return ((self.rowPosition + 1) * int(totalMazeCols)) + self.colPosition
        else:
            return -1

    # defines method for getting leftWalkable value
    def getLeftWalkable(self):
        return self.leftWalkable

    # defines method for getting rightWalkable value
    def getRightWalkable(self):
        return self.rightWalkable

    # defines method for getting topWalkable value
    def getTopWalkable(self):
        return self.topWalkable

    # defines method for getting bottomWalkable value
    def getBottomWalkable(self):
        return self.bottomWalkable

    # defines method for getting the node's fValue for A*
    def getFValue(self):
        return int(self.fValue)

    # defines method for getting the node's parent's index
    def getParentIndex(self):
        return self.parentIndex

    # defines method for knowing if this node has a left neighbor
    def hasLeftNeighbor(self):
        return (self.colPosition - 1) >= 0

    # defines method for knowing if this node has a right neighbor
    def hasRightNeighbor(self, totalMazeCols):
        return (self.colPosition + 1) < totalMazeCols

    # defines method for knowing if this node has a right neighbor
    def hasTopNeighbor(self):
        return (self.rowPosition - 1) >= 0

    # defines method for knowing if this node has a right neighbor
    def hasBottomNeighbor(self, totalMazeRows):
        return (self.rowPosition + 1) < totalMazeRows

    # defines method for knowing if this node is the start of the maze
    def isStartOfMaze(self):
        return self.isStartOfMaze

    # defines method for knowing if this node is the end of the maze
    def isEndOfMaze(self):
        return self.isEndOfMaze

    # defines method for knowing if this node is to the left of anotherNode
    def isLeftOf(self, anotherNode):
        # if MazeNode is left of anotherNode then return True
        return ((self.getRowPosition() == anotherNode.getRowPosition()) and (
            self.getColPosition() + 1 == anotherNode.getColPosition()))

    # defines method for knowing if this node is to the right of anotherNode
    def isRightOf(self, anotherNode):
        # if MazeNode is right of anotherNode then return True
        return ((self.getRowPosition() == anotherNode.getRowPosition()) and (
            self.getColPosition() - 1 == anotherNode.getColPosition()))

    # defines method for knowing if this node is above anotherNode
    def isAboveOf(self, anotherNode):
        # if MazeNode is above of anotherNode then return True
        return ((self.getRowPosition() + 1 == anotherNode.getRowPosition()) and (
            self.getColPosition() == anotherNode.getColPosition()))

    # defines method for knowing if this node is below anotherNode
    def isBelowOf(self, anotherNode):
        # if MazeNode is below of anotherNode then return True
        return ((self.getRowPosition() - 1 == anotherNode.getRowPosition()) and (
            self.getColPosition() == anotherNode.getColPosition()))

    # defines method for opening up a walkable path between Maze Node's left neighbor
    def setLeftWalkable(self):
        self.leftWalkable = True

    # defines method for opening up a walkable path between Maze Node's right neighbor
    def setRightWalkable(self):
        self.rightWalkable = True

    # defines method for opening up a walkable path between Maze Node's Top neighbor
    def setTopWalkable(self):
        self.topWalkable = True

    # defines method for opening up a walkable path between Maze Node's bottom neighbor
    def setBottomWalkable(self):
        self.bottomWalkable = True

    # defines method for setting the node's fValue for A*
    def setFValue(self, newValue):
        self.fValue = newValue

    # defines method for setting the node's parentIndex
    def setParentIndex(self, index):
        self.parentIndex = index

    # defines method for setting the node as the start of the maze
    def setAsStartOfMaze(self):
        self.isStartOfMaze = True
        self.setTopWalkable()

    # defines method for setting the node as the end of the maze
    def setAsEndOfMaze(self):
        self.isEndOfMaze = True
        self.setBottomWalkable()
