# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            leftSum = max(0,dfs(node.left)) #OPT(left)
            rightSum = max(0,dfs(node.right)) #OPT(right)

            # OPT(node)
            nodeSum = node.val + max(leftSum,rightSum)
            # local 
            localMax = node.val + leftSum + rightSum

            self.maxSum = max(self.maxSum,localMax)
            return nodeSum
        
        dfs(root)
        return self.maxSum
