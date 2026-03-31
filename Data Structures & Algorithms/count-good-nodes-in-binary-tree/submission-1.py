# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS 
        # easy way
        self.total = 0
        # def dfs(root,path):
        #     if not root:
        #         return 0
        #     if not path or root.val >= max(path):
        #         self.total += 1

        #     path.append(root.val)
        #     dfs(root.left,path)
        #     dfs(root.right,path)
        #     path.pop()

        # efficient way

        def dfs(root,maximum):
            if not root:
                return 
            if root.val >= maximum:
                self.total += 1
            new_max = max(maximum,root.val)
            dfs(root.left,new_max)
            dfs(root.right,new_max)
        
        
        dfs(root,root.val)
        return self.total

        