# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # no root
        
        if not root:
            return TreeNode(val)
        # if we to the left
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                # create it 
                root.left = TreeNode(val)
        else:
            # to the right
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val)
        return root
            