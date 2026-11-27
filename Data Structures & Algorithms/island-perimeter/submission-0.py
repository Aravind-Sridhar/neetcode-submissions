class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    perimeter+=self.explore(grid, r,c,visited)
    
        return perimeter

    def explore(self, grid, r, c, visited):
        count = 0
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 1 # found boundary (edge of land)
        if (r,c) in visited:
            return 0
        visited.add((r,c))

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

 