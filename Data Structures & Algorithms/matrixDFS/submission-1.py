class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid,r,c,visited):
            
            Rows, Cols = len(grid), len(grid[0])
            # check condition
            # 1. out of bound, visited, blocked
            if (min(r,c) < 0 or 
                r == Rows or c == Cols or 
                (r,c) in visited or grid[r][c] == 1):
                return 0
            # if we reach the end (last row and last column), return path
            #  we should reach botoom right corner
            if r == Rows - 1 and c == Cols - 1:
                return 1
            visited.add((r,c)) # add this row and the col
            # start counting
            count = 0
            #  check all directions (r-1)

            count += dfs(grid, r + 1,c,visited)
            count += dfs(grid, r - 1,c,visited)
            count += dfs(grid, r,c + 1,visited)
            count += dfs(grid, r,c - 1,visited)

            # backtrack
            visited.remove((r,c))
            # print("Paths:", visited)
            return count
        return dfs(grid,0,0,set())