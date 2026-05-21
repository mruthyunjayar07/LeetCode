from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        er, ec = entrance
        
        queue = deque([(er, ec, 0)])  # (row, col, steps)
        maze[er][ec] = '+'           # Mark entrance as visited
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if maze[nr][nc] == '+':
                    continue
                
                if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                    return steps + 1
                
                maze[nr][nc] = '+'   # Mark visited
                queue.append((nr, nc, steps + 1))
        
        return -1