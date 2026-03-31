# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d1,d2 = 0,0

        right = root.right
        left = root.left

        #  no child: only root exists: 1 node
        if not left and not right:
            return 1
        # we have 1 child 
        # two chilren at the same time
        # print("root:", root.val)
        # print(left.val if left else None,":",right.val if right else None)
        # # real stuffs
        d1 =  1 + self.maxDepth(left)
        d2 = 1 + self.maxDepth(right)
        return max(d1,d2)



        
        
        
        