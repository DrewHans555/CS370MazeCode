# This class creates a Maze Node object that knows it's position in the maze array.
# Each Maze Node should be thought of as an open space surrounded by four walls with 
# the position (rowPosition, colPosition) in a maze of size (totalRows, totalCols).
# When you want to open up a walkable path between two nodes you must set the 
# nodes opposite walkable boolean variables to TRUE (so rightWalkable = True for node 1
# and leftWalkable = True for node 2 implies that there is no wall between nodes 1 and 2).

class MazeNode:
    # defines constructor for MazeNode class
    def __init__(self, rowPos=0, colPos=0):
        self.rowPosition = rowPos
        self.colPosition = colPos

        # walkable = False means that a wall exists between nodes
        self.leftWalkable = False
        self.rightWalkable = False
        self.topWalkable = False
        self.bottomWalkable = False

        # openable = True means that a path can be created
        self.leftOpenable = True
        self.rightOpenable = True
        self.topOpenable = True
        self.bottomOpenable = True

    # defines representation for Python Interpreter
    def __repr__(self):
        return repr([self.rowPosition, self.colPosition])

    # defines the string that gets displayed when printing the node
    def __str__(self):
        return "(" + str(self.rowPosition) + "," + str(self.colPosition) + ")"

    # defines the method for getting the node's row position
    def getRowPosition(self):
        return self.rowPosition

    # defines the method for getting the node's column position
    def getColPosition(self):
        return self.colPosition

    # defines method for getting position of MazeNode's left neighbor's rowPosition
    def getLeftNeighborRowPosition(self):
        if (self.colPosition - 1) >= 0:
            return self.rowPosition
        else:
            return None

    # defines method for getting position of MazeNode's left neighbor's colPosition
    def getLeftNeighborColPosition(self):
        if (self.colPosition - 1) >= 0:
            return self.colPosition - 1
        else:
            return None

    # defines method for getting position of MazeNode's top neighbor's rowPosition
    def getTopNeighborRowPosition(self):
        if (self.rowPosition - 1) >= 0:
            return self.rowPosition - 1
        else:
            return None

    # defines method for getting position of MazeNode's top neighbor's colPosition
    def getTopNeighborColPosition(self):
        if (self.rowPosition - 1) >= 0:
            return self.colPosition
        else:
            return None

    # defines method for getting position of MazeNode's right neighbor's rowPosition
    def getRightNeighborRowPosition(self, totalMazeCols):
        if (self.colPosition + 1) < totalMazeCols:
            return self.rowPosition
        else:
            return None

    # defines method for getting position of MazeNode's right neighbor's colPosition
    def getRightNeighborColPosition(self, totalMazeCols):
        if (self.colPosition + 1) < totalMazeCols:
            return self.colPosition + 1
        else:
            return None

    # defines method for getting position of MazeNode's bottom neighbor's rowPosition
    def getBottomNeighborRowPosition(self, totalMazeRows):
        if (self.rowPosition + 1) < totalMazeRows:
            return self.rowPosition + 1
        else:
            return None

    # defines method for getting position of MazeNode's bottom neighbor's colPosition
    def getBottomNeighborColPosition(self, totalMazeRows):
        if (self.rowPosition + 1) < totalMazeRows:
            return self.colPosition
        else:
            return None

    # defines method for getting leftOpenable value
    def getLeftOpenable(self):
        return self.leftOpenable

    # defines method for getting rightOpenable value
    def getRightOpenable(self):
        return self.rightOpenable

    # defines method for getting topOpenable value
    def getTopOpenable(self):
        return self.topOpenable

    # defines method for getting bottomOpenable value
    def getBottomOpenable(self):
        return self.bottomOpenable

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

    # defines method for knowing if a path can be made to the Maze Node's left neighbor
    def setLeftOpenable(self, boolean):
        self.leftOpenable = boolean

    # defines method for knowing if a path can be made to the Maze Node's right neighbor
    def setRightOpenable(self, boolean):
        self.rightOpenable = boolean

    # defines method for knowing if a path can be made to the Maze Node's top neighbor
    def setTopOpenable(self, boolean):
        self.topOpenable = boolean

    # defines method for knowing if a path can be made to the Maze Node's bottom neighbor
    def setBottomOpenable(self, boolean):
        self.bottomOpenable = boolean

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
