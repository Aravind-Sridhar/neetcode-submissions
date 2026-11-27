from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS - from each node - add it as dist in visited and replace val in original grind
        queue = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c, 0))
        for val in queue:
            r,c,d = val
            visited.add((r,c))
        while queue:
            r,c, dist = queue.popleft()
            directions = [
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            ]

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or (nr,nc) in visited:
                    continue
                if grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] == 2147483647 and (nr,nc) not in visited:
                    grid[nr][nc] = dist+1
                    visited.add((nr,nc))
                    queue.append((nr,nc,dist+1))
