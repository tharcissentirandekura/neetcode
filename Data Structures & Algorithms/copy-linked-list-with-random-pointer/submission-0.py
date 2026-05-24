"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use hashtable to store elements and they index
        copies = {None:None}

        # iterate through the list 
        # store the node with each copy
        curr = head
        while curr:
            curr_copy = Node(curr.val)
            copies[curr] = curr_copy
            curr = curr.next

        curr = head
        while curr:
            # get the current Node copy
            copy = copies[curr]
            # connect the next with the curr node copy next node
            copy.next = copies[curr.next]
            # same with the random
            copy.random = copies[curr.random]

            curr = curr.next
        return copies[head]

        