# This class creates a standard Stack data struture.
class Stack:
    # defines constructor for Stack class
    def __init__(self, name='stack'):
        self.name = name
        self.nodes = []

    # defines method for checking stack for nodes
    def isEmpty(self):
        return self.nodes == []

    # defines method for adding nodes to stack
    def push(self, node):
        self.nodes.append(node)

    # defines method for removing last added node from stack
    def pop(self):
        return self.nodes.pop()

    # defines method for looking at last added node in stack
    def peek(self):
        return self.nodes[len(self.nodes) - 1]

    # defines method for getting the number of nodes in stack
    def size(self):
        return len(self.nodes)