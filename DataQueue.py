# This class creates a standard Queue data struture.
class Queue:
    # defines constructor for Queue class
    def __init__(self, name='queue'):
        self.name = name
        self.nodes = []

    # defines method for checking queue for nodes
    def isEmpty(self):
        return self.nodes == []

    # defines method for adding nodes to queue
    def enqueue(self, node):
        self.nodes.insert(0, node)

    # defines method for removing first node from queue
    def dequeue(self):
        return self.nodes.pop()

    # defines method for getting the number of nodes in queue
    def size(self):
        return len(self.nodes)
        
