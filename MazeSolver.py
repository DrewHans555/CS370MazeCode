# This class generates a Maze

from Maze import Maze
from MazeNode import MazeNode


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, mazeRows, mazeCols):
        self.listOfMazeNodes = []
        self.generateMaze(mazeRows, mazeCols)

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.listOfMazeNodes

    # defines method for building a new maze
    def generateMaze(self, totalRows, totalCols):
        # get the list of MazeNodes from new
        self.listOfMazeNodes = Maze(totalRows, totalCols).getMazeArray()


MazeSolver(50, 50)
