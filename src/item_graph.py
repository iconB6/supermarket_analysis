from collections import defaultdict
from itertools import combinations

class ItemGraph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_transaction(self, items):
        unique_items = set(items)
        for a, b in combinations(unique_items, 2):
            self.graph[a][b] += 1
            self.graph[b][a] += 1

    # Linear Search implementation
    def is_frequently_bought(self, item_a, item_b, threshold):
        if item_a not in self.graph:
            return False

        for neighbor, freq in self.graph[item_a].items():
            if neighbor == item_b:
                return freq >= threshold

        return False
    
    # DFS traversal for item association discovery
    def dfs_related_items(self, start):
        visited = set()

        def dfs(item):
            for neighbor in self.graph[item]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        if start not in self.graph:
            return visited

        dfs(start)
        return visited
    


