# This class takes in a Maze, as a list of MazeNode objects (each knowing if they are the start/ end of the maze,
# and which of their sides have walls or walkable space), and returns a solution to the maze using a path-finding
# algorithm (depth-first-search, breadth-first-search, A*, etc.).

from collections import deque  # needed for creating a queue for breadth first search
import queue  # needed for creating a priority queue for a star
import sys


class MazeSolver:
    # defines constructor for MazeGenerator class
    def __init__(self, mazeObject):
        self.mazeNodes = mazeObject.getMazeArray()
        self.mazeRows = mazeObject.getTotalRows()
        self.mazeCols = mazeObject.getTotalCols()
        self.startIndex = mazeObject.getStartNodeIndex()
        self.endIndex = mazeObject.getEndNodeIndex()

        # reset the recursion limit for large mazes to prevent crashing
        if self.mazeRows * self.mazeCols > sys.getrecursionlimit():
            sys.setrecursionlimit(self.mazeRows * self.mazeCols + 5)

        self.nodesExplored = 0
        self.solutionPath = []

    # defines representation for Python Interpreter
    def __repr__(self):
        return self

    # defines method for solving with a recursive depth-first search algorithm
    def solveWithDFS(self):
        # set up visitedNodes stack and push start node's index
        stack = []
        stack.append(self.startIndex)

        # now that setup is complete do the recursive depth-first search
        self.depthFirstSearch(stack)
        return self.solutionPath

    # defines method for getting the solution path with DFS
    def depthFirstSearch(self, stack):
        self.nodesExplored = self.nodesExplored + 1

        # get the last added node index from the stack
        nodeIndex = stack.pop()
        node = self.mazeNodes[nodeIndex]

        # get the neighbor node indexes of neighbors that can be walked to from current node
        neighborNodeIndexes = self.getLegalNeighborNodeIndexes(node)

        # add the current node index to the stack of visited node's indexes
        stack.append(nodeIndex)

        if neighborNodeIndexes:
            # for each neighbor node
            for x in range(len(neighborNodeIndexes)):
                neighborNodeIndex = neighborNodeIndexes[x]
                neighborNode = self.mazeNodes[neighborNodeIndex]

                if neighborNode.isMazeEnd():
                    # set parent index for getting the solution path
                    neighborNode.setParentIndex(node.getIndexInMazeArray())
                    return self.getSolutionPath(neighborNode)
                if neighborNodeIndex not in stack:
                    # set parent index for getting the solution path later
                    neighborNode.setParentIndex(node.getIndexInMazeArray())

                    # add the unvisited node index to the stack to be carried to the next dfs iteration
                    stack.append(neighborNodeIndex)

                    # do dfs for last neighborNodeIndex pushed to the stack
                    self.depthFirstSearch(stack)

    # defines method for solving with a recursive breadth-first search algorithm
    def solveWithBFS(self):
        # set up checkedNodes list and uncheckedNodesQ queue and then enqueue start node's index
        checkedNodes = []
        uncheckedNodesQ = deque()
        uncheckedNodesQ.append(self.startIndex)

        # now that setup is complete do the recursive depth-first search
        self.breadthFirstSearch(checkedNodes, uncheckedNodesQ)
        return self.solutionPath

    # defines method for getting the solution path with BFS
    def breadthFirstSearch(self, checkedNodes, uncheckedNodesQ):
        self.nodesExplored = self.nodesExplored + 1

        # get the first added node index from the queue
        nodeIndex = uncheckedNodesQ.popleft()
        node = self.mazeNodes[nodeIndex]

        # get the neighbor node indexes of neighbors that can be walked to from current node
        neighborNodeIndexes = self.getLegalNeighborNodeIndexes(node)

        # add the current node index to the queue of checked node's indexes
        checkedNodes.append(nodeIndex)

        if neighborNodeIndexes:
            # for each neighbor node
            for x in range(len(neighborNodeIndexes)):
                neighborNodeIndex = neighborNodeIndexes[x]
                neighborNode = self.mazeNodes[neighborNodeIndex]

                if neighborNode.isMazeEnd():
                    # set parent index for getting the solution path
                    neighborNode.setParentIndex(nodeIndex)
                    return self.getSolutionPath(neighborNode)
                if neighborNodeIndex not in checkedNodes:
                    # set parent index for getting the solution path
                    neighborNode.setParentIndex(nodeIndex)

                    # add the unchecked node index to the queue to be carried to the next bfs iteration
                    uncheckedNodesQ.append(neighborNodeIndex)

        # do bfs for first neighborNodeIndex in the queue
        self.breadthFirstSearch(checkedNodes, uncheckedNodesQ)

    # defines method for solving with a recursive A* Algorithm
    def solveWithAStar(self):
        # set up openNodePQ priority queue and checkedNodes list
        openNodePQ = queue.PriorityQueue(0)
        checkedNodes = []

        # set the values for the starting node and put it in the priority queue
        self.mazeNodes[self.startIndex].setFValue(0)
        self.mazeNodes[self.startIndex].setGValue(0)
        self.mazeNodes[self.startIndex].setHValue(0)
        openNodePQ.put([0, self.startIndex])

        # now that setup is complete do the recursive A* search
        self.aStarSearch(openNodePQ, checkedNodes)

        return self.solutionPath

    # defines method for getting the solution path with a recursive A* Algorithm
    def aStarSearch(self, openNodesPQ, checkedNodes):
        self.nodesExplored = self.nodesExplored + 1

        # get the node index with lowest f value from the openNodesPQ
        nodeIndex = openNodesPQ.get()[1]
        currentNode = self.mazeNodes[nodeIndex]

        # get the neighbor node indexes of neighbors that can be walked to from current node
        neighborNodeIndexes = self.getLegalNeighborNodeIndexes(currentNode)

        if neighborNodeIndexes:
            # for each neighbor node
            for x in range(len(neighborNodeIndexes)):
                neighborNodeIndex = neighborNodeIndexes[x]
                neighborNode = self.mazeNodes[neighborNodeIndex]

                if neighborNode.isMazeEnd():
                    # set parent index for getting the solution path
                    neighborNode.setParentIndex(currentNode.getIndexInMazeArray())
                    return self.getSolutionPath(neighborNode)
                if neighborNodeIndex not in checkedNodes and self.is_not_in_queue(neighborNodeIndex, openNodesPQ):
                    # set parent index for getting the solution path
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
                        # set parent index for getting the solution path
                        neighborNode.setParentIndex(currentNode.getIndexInMazeArray())

                        # set the neighbor node's fValue, gValue, and hValue
                        newFValue = newGValue + neighborNode.getHValue()
                        neighborNode.setGValue(newGValue)
                        neighborNode.setFValue(newFValue)

                        # when finished add it to the priority queue then go to next neighbor
                        openNodesPQ.put([newFValue, neighborNodeIndex])
                # add current node to checkedNodes after exploring all neighbors
            checkedNodes.append(currentNode.getIndexInMazeArray())
            # do a* for the next lowest fValue node in openNodesPQ
            self.aStarSearch(openNodesPQ, checkedNodes)

    # define method getting the indexs of legal, walkable neighbor nodes
    def getLegalNeighborNodeIndexes(self, currentNode):
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
            return gValueOfThisNode + 25
        elif givenNode.isLeftOf(node) or givenNode.isRightOf(node):
            # moving left or right keeps you at the same level (so moderate cost)
            return gValueOfThisNode + 15
        elif givenNode.isBelowOf(node):
            # moving down gets you closer to the bottom row where the goalNode is (so lower cost)
            return gValueOfThisNode + 5
        else:
            # only return -1 if something goes horribly wrong
            return -1

    # defines method for getting the heuristic value of a node
    def calculateHValue(self, node):
        # given two points P(p1,p2) and Q(q1,q2), the taxicab distance D between P and Q is
        # given by the equation D = |p1-q1| + |p2-q2|
        goalNode = self.mazeNodes[self.endIndex]
        return abs(node.getRowPosition() - goalNode.getRowPosition()) + abs(
            node.getColPosition() - goalNode.getColPosition())

    # defines method for getting the total number of nodes explored while solving
    def getNodesExplored(self):
        return self.nodesExplored

    # defines method for getting the solution path after the maze has been solved
    def getSolutionPath(self, node):
        # add node path from end to start
        string = "(" + str(node.getRowPosition()) + "," + str(node.getColPosition()) + ")"
        self.solutionPath.append(string)

        # if node's parent index = -1 then you've reached the start node
        if node.getParentIndex() == -1:
            # reverse the list so that it prints the path from start node to end node
            self.solutionPath.reverse()
            return self.solutionPath
        else:
            self.getSolutionPath(self.mazeNodes[node.getParentIndex()])

    # defines method for knowing if x is in a q
    # http://stackoverflow.com/questions/22737111/check-if-something-is-already-in-priority-queue-python
    def is_in_queue(self, x, q):
        with q.mutex:
            return x in q.queue

    # defines method for knowing if x is not in a q
    # http://stackoverflow.com/questions/22737111/check-if-something-is-already-in-priority-queue-python
    def is_not_in_queue(self, x, q):
        with q.mutex:
            return not (x in q.queue)
