from search import *
from utils import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial=('F', 'G', 'W', 'C'), goal=()):
        self.initial = initial
        self.goal = goal
        super().__init__(self.initial, self.goal)

    def actions(self, state):
        possible_crossings = []
        for i in state:
            for j in state:
                if i != j:
                    crossing = tuple(sorted(set(state) - set((i, j))))
                    if self.is_valid_crossing(crossing, state):
                        possible_crossings.append(crossing)
        return possible_crossings

    def result(self, state, action):
        return tuple(sorted(set(state) - set(action)))

    def goal_test(self, state):
        return state == self.goal

    def is_valid_crossing(self, crossing, state):
        left_bank = tuple(sorted(set(state) - set(crossing)))
        return self.is_valid(left_bank) and self.is_valid(crossing)

    def is_valid(self, objects):
        if 'F' not in objects:
            return True
        if 'G' in objects and 'C' in objects:
            return False
        if 'W' in objects and 'G' in objects:
            return False
        return True


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    print('We start with members {} on the left side but want {} on the left side at the end '.format(wgc.initial, wgc.goal))

    # Depth-first search
    dfs_solution = depth_first_graph_search(wgc)
    if dfs_solution:
        print("DFS Solution:", dfs_solution.solution())
    else:
        print("DFS: No solution found.")

    # Breadth-first search
    bfs_solution = breadth_first_graph_search(wgc)
    if bfs_solution:
        print("BFS Solution:", bfs_solution.solution())
    else:
        print("BFS: No solution found.")
