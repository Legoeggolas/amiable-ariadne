from util.graph import Node
from collections import deque


class MazeProcessor:

    def __init__(self, maze: list):
        self.start = None
        self.end = None
        self.maze = maze
        self.process()

    def process(self):
        length = len(self.maze[0])
        width = len(self.maze)
        column_buffer = [None] * length
        row_last_node = None

        # Most mazes have their entrance in the first row
        # Except for unicursal
        for col in range(0, length):
            if self.maze[0][col] == 0:
                if not self.start:
                    self.start = Node((0, col))
                    column_buffer[col] = self.start
                else:
                    self.end = Node((0, col))
                    column_buffer[col] = self.end
                    break

        # Iterate over the main body of the maze
        for row in range(1, width - 1):
            row_last_node = None  # Each row starts with no leftmost node

            for col in range(1, length - 1):

                # Check if the current position represents a wall
                if self.maze[row][col] == 1:

                    row_last_node = None
                    column_buffer[col] = None
                    continue

                # This node might not be needed
                # But in case it is, it makes any checks a lot easier
                node = Node((row, col))

                # Check based on whether a passage downwards exists
                if self.maze[row + 1][col] == 0:

                    # There is a passage on the left
                    if row_last_node:
                        node.neighbours[2] = row_last_node
                        row_last_node.neighbours[3] = node

                        # There is a vertical passage passing through this node
                        if column_buffer[col]:
                            node.neighbours[0] = column_buffer[col]
                            column_buffer[col].neighbours[1] = node

                        row_last_node = node
                        column_buffer[col] = node
                    else:
                        # Check if this is the start of a new horizontal passage
                        if self.maze[row][col + 1] == 0:
                            # Check if there is a vertical passage above
                            if column_buffer[col]:
                                node.neighbours[0] = column_buffer[col]
                                column_buffer[col].neighbours[1] = node

                            row_last_node = node
                            column_buffer[col] = node

                        if column_buffer[col] and not row_last_node:
                            # Currently in the middle of a vertical passage
                            # No need to add this node to the graph
                            continue
                        else:
                            # Otherwise this is the start of a vertical passage
                            column_buffer[col] = node
                else:

                    # Check if this is the end of a vertical passage
                    if column_buffer[col]:
                        node.neighbours[0] = column_buffer[col]
                        column_buffer[col].neighbours[1] = node

                        # Check if the node is a part of a horizontal passage
                        if row_last_node:
                            node.neighbours[2] = row_last_node
                            row_last_node.neighbours[3] = node

                        row_last_node = node
                        column_buffer[col] = node
                    else:
                        # Check if in the middle of a horizontal passage
                        if row_last_node:
                            if self.maze[row][col + 1] == 0:
                                # We are, so no need to add this node to the graph
                                continue
                            else:
                                # This is the end of a horizontal passage
                                node.neighbours[2] = row_last_node
                                row_last_node.neighbours[3] = node

                            row_last_node = node
                        else:
                            # Check if at the beginning of a new horizontal passage
                            if self.maze[row][col + 1] == 0:
                                row_last_node = node
                            # Otherwise we are in between walls on all four sides
                            # which should never happen

        # Most mazes have their exits in the last row
        # But if the maze was a unicursal one, the end has already been found
        if self.end:
            return
        for col in range(0, length):
            if self.maze[width - 1][col] == 0:
                self.end = Node((width - 1, col))

                if column_buffer[col]:
                    self.end.neighbours[0] = column_buffer[col]
                    column_buffer[col].neighbours[1] = self.end
                break

    # Debugging function
    # Print the positions of all generated nodes, together with their neighbours
    def _print_graph(self):
        visited = set()
        with open("test.txt", "w") as file:
            q = deque()
            q.append(self.start)

            while q:
                curr = q.popleft()
                visited.add(curr)
                file.write(
                    f"{curr.position} : {[node.position if node else None for node in curr.neighbours]}\n"
                )
                for node in curr.neighbours:
                    if node and node not in visited:
                        q.append(node)
