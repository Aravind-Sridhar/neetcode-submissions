class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r,c,visited):
                    count+=1
        
        return count


    def explore(self, grid, r, c, visited):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return False
        if grid[r][c] == "0":
            return False
        
        if (r,c) in visited:
            return False
        
        visited.add((r,c))
        

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        for dr, dc in directions:
            nr = r+dr
            nc = c+dc

            self.explore(grid,nr,nc,visited)

        return True

        