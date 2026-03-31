# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS traversal technique

        if not root:
            return []
        queue = deque()
        results = []
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                current_node = queue.popleft()
                level_nodes.append(current_node.val)

                # add their chilren in the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            # add the local node list to the result
            results.append(level_nodes)
        return results

