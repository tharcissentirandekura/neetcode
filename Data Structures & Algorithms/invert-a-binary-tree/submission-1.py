# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # preorder
        if root is None:
            return None
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp


        elif root.left and not root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
            # self.invertTree(root.left)

        elif root.right and not root.left:
            temp = root.right
            root.right = root.left
            root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

