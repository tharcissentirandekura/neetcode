# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Find hight of subtree and right
        # if one differs by more than 1

        self.counts = 0
        def height(node:Optional[TreeNode]):
            if not node:
                return 0
            left = height(node.left) #left height
            if left == -1 :
                return -1
            right = height(node.right) #right height
            if right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return 1 + max(left,right)
        
        return height(root) != -1



        