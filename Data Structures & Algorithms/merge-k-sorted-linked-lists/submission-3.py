# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        for i in range(1,len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])
        return lists[-1]
        
    # a helper to merge two lists
    def merge(self,l1,l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            # check which one is smaller
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # add remaining because one of them is bigger
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    

        














