from collections import deque
from util.graph import Node
from maze.draw import DrawBuffer
from random import choice, choices


# A pathfinder that travels randomly
def tourist(start: Node, end: Node, buffer: DrawBuffer, explore_color: tuple) -> list:
    visited = set()

    pi = dict()
    pi[start] = None

    curr = start

    while curr != end:
        if curr not in visited:
            buffer.push(pi[curr], curr, explore_color)

        visited.add(curr)
        viable_neighbours = [node for node in curr.neighbours if node and node not in visited]
        if not viable_neighbours:
            curr = pi[curr]
            continue

        next_node = choice(viable_neighbours)
        pi[next_node] = curr
        curr = next_node

    path = list()
    tail = end
    while tail:
        path.append(tail)
        tail = pi[tail]

    return path
