"""Node module have single node"""

class Node:
    """Node class which will initiate a node with data and two child."""
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        