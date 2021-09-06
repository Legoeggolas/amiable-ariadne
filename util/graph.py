# A simple node
# Stores the position as a tuple of abscissa and ordinate
# Also stores other neighbouring Nodes in an ordered list
class Node:

    def __init__(self, position: tuple):
        self.position = position
        self.neighbours = [None, None, None, None]  # Up, Down, Left, Right