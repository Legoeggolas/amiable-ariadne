class Node:

    def __init__(self, position: tuple):
        self.position = position
        self.neighbours = [None, None, None, None]  # Up, Down, Left, Right