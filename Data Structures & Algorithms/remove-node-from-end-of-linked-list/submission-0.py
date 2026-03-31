# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use slow and fast pointers 
        dummy = ListNode(0,head)

        slow = dummy
        fast = dummy

        # advance fast
        for _ in range(n + 1):
            if fast:
                fast = fast.next
        while fast: #as long as the fast is still not None
            fast = fast.next
            slow = slow.next #move slow up to n - 2
        print("Fast:",fast.val if fast else None)
        slow.next = slow.next.next
        return dummy.next  






            