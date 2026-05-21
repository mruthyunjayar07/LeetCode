class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], 
                     queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val
        
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited = set()
            queue = deque([(src, 1.0)])  # (current_node, accumulated_product)
            
            while queue:
                node, product = queue.popleft()
                if node == dst:
                    return product
                visited.add(node)
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * weight))
            
            return -1.0  # No path found
        
        return [bfs(c, d) for c, d in queries]