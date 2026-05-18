class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        visited = {0}
        queue = deque([0])
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                
                neighbors = [i + 1, i - 1] + graph[arr[i]]
                
                graph[arr[i]].clear()
                
                for j in neighbors:
                    if j == n - 1:
                        return steps
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)
        
        return steps