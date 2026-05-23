# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
        We must merge k first nodes in linkedList then next k nodes 
        if there are fewer than k nodes left, leae the nodes as they are

        eg:
        list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 and k = 3
        result = reverse(1 -> 2 -> 3 ) and reverse(4 -> 5 -> 6)
        
        Idea: devide the lists into k equals groups and alternate
        reverse first k and then next k

        - iterate through elemetnts up to k while reversing and move forward
        - we need to know the size to decide whether or not we reverse it or not
        """

        def getKthNode(curr,k):
            while curr and k > 0:
                curr = curr.next
                k-=1
            return curr #kth node
            
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True: # we have k nodes in the group
            kthNode = getKthNode(groupPrev,k)
            if not kthNode:
                break
            groupNext = kthNode.next
            # reverse groupPrev.next up to kth node
            prev = groupNext
            curr = groupPrev.next
            # check if we haven't reached the kth node
            while curr != groupNext: 
                # point next
                nxt = curr.next
                # reverse the pointer
                curr.next = prev
                # move prev forward
                prev = curr
                # move curr forward
                curr = nxt
            
            # reconnect the reversed group
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp

        return dummy.next

        


            

        