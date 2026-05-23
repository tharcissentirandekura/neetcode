# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merging 2 for example
        """
            This requires to go through the list : O(k)
            traverse k list at time
        """
        res = ListNode() #create new head
        listIndex = 0
        itemIndex = 0

        # O(n) time complexity with n max element in array
        def merge(l1:ListNode,l2: ListNode):
            res = ListNode()
            head = res
            while l1 and l2:
                # check which one is smaller
                if l1.val < l2.val:
                    newNode = ListNode(l1.val);
                    head.next = newNode
                    head = newNode #make it the head
                    l1 = l1.next
                else:
                    newNode = ListNode(l2.val);
                    head.next = newNode
                    head = newNode
                    l2 = l2.next
            # add remaining because one of them is bigger
            while l1:
                newNode = ListNode(l1.val);
                head.next = newNode
                head = newNode #make it the head
                l1 = l1.next
            while l2:
                newNode = ListNode(l2.val);
                head.next = newNode
                head = newNode
                l2 = l2.next
            return res.next
        
        # we need to iterate in kth array
        #  we can use devide and conquer where we split the lists into 2 halfgs and merge those

        # recursive: Expensive
        # def mergeSort(lists):
        #     if len(lists) == 0:
        #         return None
        #     if len(lists) == 1:
        #         return lists[0]
        #     # split in two
        #     mid = len(lists) // 2
        #     # recursively call 
        #     left = mergeSort(lists[:mid])
        #     right = mergeSort(lists[mid:])
        #     return merge(left,right)

        # iteravice: merge(lists[i],lists[i-1]) and store that in lists[i]
        def mergeSort(lists):
            if len(lists) == 0:
                return None
            if len(lists) == 1:
                return lists[0]
            for i in range(1,len(lists)):
                merged = merge(lists[i - 1], lists[i])
                lists[i] = merged
            return lists[-1]
        return mergeSort(lists)



        














