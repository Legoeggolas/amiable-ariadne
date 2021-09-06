from .breadthfirst import breadth_first_search
from .depthfirst import depth_first_search
from .tourist import tourist

from util.inpututils import take_input


# An interface class for all the pathfinder methods
# Helps select which one is to be used outside of the submodule
class Pathfinder:

    def __init__(self) -> None:
        self.dispatch = dict()

        self.dispatch["bfs"] = breadth_first_search
        self.dispatch["dfs"] = depth_first_search
        self.dispatch["tourist"] = tourist

    def pick(self):
        pfinder = take_input(str,
                             "Enter the algorithm you wish to use: ",
                             scope=self.dispatch.keys())

        return self.dispatch[pfinder]