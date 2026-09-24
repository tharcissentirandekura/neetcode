class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])

        count = 0

        def dfs(grid,r,c):
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or grid[r][c] == '0':
                return 
            
            # mark it
            grid[r][c] = '0'

            # visit all connected to it
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid,r,c)

        
        return count



                 

        


