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
