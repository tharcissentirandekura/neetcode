# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list into two halves
        # get the second part
        # if not head or head.next:
        #     return 
        fast_ptr = head.next
        slow_ptr = head #this is the second part of the list

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        # reverse the second list

        prev = None
        curr = slow_ptr
        nextNode = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # time to merge
        l1 = head
        l2 = prev #second

        while l2:
            temp1,temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            if not temp1:
                break
            l1,l2 = temp1,temp2
        
        return 
            
            
        

        
