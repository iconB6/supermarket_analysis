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
    
    # Merge sort ranking co-purchased items
    def merge_sort(self, items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = self.merge_sort(items[:mid])
        right = self.merge_sort(items[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] >= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_top_co_purchased(self, item, k=3):
        if item not in self.graph:
            return []

        pairs = list(self.graph[item].items())
        sorted_pairs = self.merge_sort(pairs)
        return sorted_pairs[:k]
    
    # Recommendation-style query
    def recommend_items(self, basket, k=3):
        """
        Recommend items likely to be bought together with the given basket.
        """
        scores = defaultdict(int)

        for item in basket:
            if item not in self.graph:
                continue

            for neighbor, freq in self.graph[item].items():
                if neighbor not in basket:
                    scores[neighbor] += freq  # linear accumulation

        if not scores:
            return []

        pairs = list(scores.items())
        sorted_pairs = self.merge_sort(pairs)
        return sorted_pairs[:k]


    


