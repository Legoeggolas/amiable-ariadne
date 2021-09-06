from collections import deque
from util.graph import Node
from maze.draw import DrawBuffer


def depth_first_search(start: Node, end: Node, buffer: DrawBuffer, explore_color: tuple) -> list:
    visited = set()

    pi = dict()
    pi[start] = None

    q = deque()
    q.append(start)

    while q:
        curr = q.pop()

        buffer.push(pi[curr], curr, explore_color)

        if curr == end:
            break

        visited.add(curr)

        for node in curr.neighbours:
            if node and node not in visited:
                q.append(node)
                pi[node] = curr

    path = list()
    tail = end
    while tail:
        path.append(tail)
        tail = pi[tail]

    return path