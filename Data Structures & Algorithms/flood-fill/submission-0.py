class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        def dfs(image,r,c,visited):
            Rows,Cols = len(image), len(image[0])
            # check out of bound
            if (min(r,c) < 0 or 
                r == Rows or c == Cols or (r,c) in visited or image[r][c] != original_color):
                return image
            if image[r][c] == original_color:
                image[r][c] = color

            visited.add((r,c))
            
            # visit the neighbors vertically and horizontally
            dfs(image,r + 1,c,visited)
            dfs(image,r - 1,c,visited)
            dfs(image,r,c + 1,visited)
            dfs(image,r,c - 1,visited)

            return image
        return dfs(image,sr,sc,set())