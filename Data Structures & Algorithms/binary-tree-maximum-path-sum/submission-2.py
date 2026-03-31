# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            # Explore each node in the left subtree.
            left = max(dfs(node.left),0) #only to include positives
            # Explore each node in the right subtree.
            right = max(dfs(node.right),0)

            local_sum = node.val + left + right
            self.max_sum = max(self.max_sum,local_sum)

            return node.val + max(left,right) 
        dfs(root)
        return self.max_sum
            