from collections import deque
from typing import Any
from util.graph import Node


# This class helps store, retreive, and draw instructions directly onto the
# graphical representation of the maze
class DrawBuffer:

    # An inner class that represents a single draw instruction
    # Each instruction corresponds to a line being drawn between the two given nodes
    # with the provided color
    class DrawBufferObj:

        def __init__(self, start: Node, end: Node, color: tuple) -> None:
            if not end:
                raise ValueError

            if start:
                self.startX = start.position[0]
                self.startY = start.position[1]
            else:
                self.startX = end.position[0]
                self.startY = end.position[1]

            self.endX = end.position[0]
            self.endY = end.position[1]

            self.color = color

    def __init__(self, data: Any) -> None:
        self.buffer = deque()
        self.img_data = data

    # Pushes an instruction at the back of the queue
    def push(self, start: tuple, end: tuple, color: tuple) -> None:
        buffer_obj = DrawBuffer.DrawBufferObj(start, end, color)
        self.buffer.append(buffer_obj)

    # Extracts an instruction from the front of the queue
    def pop(self) -> DrawBufferObj:
        # In case there is nothing in the queue
        if not self.buffer:
            return None

        curr = self.buffer.popleft()
        return curr

    # Draws the instruction to the image data
    def draw(self) -> None:
        curr = self.pop()

        if not curr:
            return

        if curr.startX == curr.endX:
            for col in range(min(curr.startY, curr.endY), max(curr.startY, curr.endY) + 1):
                self.img_data[col, curr.startX] = curr.color
        else:
            for row in range(min(curr.startX, curr.endX), max(curr.startX, curr.endX) + 1):
                self.img_data[curr.startY, row] = curr.color

    def empty(self):
        return True if len(self.buffer) == 0 else False