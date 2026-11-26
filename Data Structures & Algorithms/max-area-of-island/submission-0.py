class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        largest = 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count = self.explore(grid, r,c,visited)
            
                if count > largest:
                    largest = count
        
        return largest

    def explore(self, grid, r, c, visited):
        count =0
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 0
        if grid[r][c] == 0:
            return 0
        if (r,c) in visited:
            return 0
        visited.add((r,c))
        count+=1
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            count+=self.explore(grid, nr,nc,visited)
        
        return count

