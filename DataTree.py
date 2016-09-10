# This class creates a generic Tree data structure starting with a root node.
# The root node connects to zero or three children nodes where each child node
# is either the adjacent left node, bottom node, or right node and is also a Tree.

class Tree:
    # defines constructor for Tree class
    def __init__(self, name='rootNode'):
        self.name = name
        self.children = []

    # defines representation for Python Interpreter
    def __repr__(self):
        return self.name

    # defines method for adding children nodes to the tree
    def add_child(self, node):
        self.children.append(node)

    # defines method for getting the list of children nodes
    def get_children(self):
        return self.children
