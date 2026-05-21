from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b in connections:
            graph[a].append((b, 1))  # original: a → b (costs 1 to reverse)
            graph[b].append((a, 0))  # reverse:  b → a (free, already inward)
        
        visited = set([0])
        queue = deque([0])
        changes = 0
        
        while queue:
            node = queue.popleft()
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += cost      # cost=1 means edge points away → reverse it
                    queue.append(neighbor)
        
        return changes