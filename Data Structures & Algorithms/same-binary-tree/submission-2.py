# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(p,q):
            print(f"Compare: {p.val if p else None}{q.val if q else None}")
            
            
            if not p and not q: #Base case
                return True   


            elif not p or not q:
                return False

            
            elif p.val != q.val:
                return False
            
            else:
                return traverse(p.left,q.left) and traverse(p.right,q.right)

        return traverse(p,q)


            