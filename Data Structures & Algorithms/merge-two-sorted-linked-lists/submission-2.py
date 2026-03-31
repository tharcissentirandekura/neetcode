# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            - Check which one is bigger
            - Loop through the smallest first
            - Add the rest: Same as array
        """

        dummy = ListNode(-1)
        reshead = dummy
        
        l1 = list1
        l2 = list2

        # merge
        while l1 and l2:
            if l1.val <= l2.val:
                reshead.next = l1
                l1 = l1.next
            else:
                reshead.next = l2
                l2 = l2.next
            reshead = reshead.next
            # small = reshead
            

        # append the rest
        print(f"{reshead.next.val if reshead.next else None}")
        if l1:
            # add remaining values to reshead
            reshead.next = l1

        if l2:
            # add remaining values to reshead
            reshead.next = l2
        return dummy.next
            


        

            
        



        
