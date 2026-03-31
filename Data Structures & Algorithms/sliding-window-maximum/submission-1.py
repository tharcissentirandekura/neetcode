class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use a deque for optimization
        # queue will hold the values in the window
        # every time we want to add one we add to queue adn remove to it
        # The brute force, compute max at every window
        # front is index of max in window
        q = deque() #for index

        # this is a fixed window
        window = nums[:k]

        slide_max = max(nums)




        res = []
        
        # for i in range(len(nums) - k):
        #     res.append(max(window))
        #     # remove one and add one
        #     window = nums[i + 1: i + k + 1]
        # res.append(max(nums[len(nums) - k: len(nums)]))
        # return res

        left,right = 0,0
        while right < len(nums):
            # remove from current window
            # nums[q[-1]]  would never be max as long as nums[right] is in this window
            while q and nums[q[-1]] < nums[right]:
                q.pop() #take it out
            q.append(right) #add right
            # q[0] is outside the current window.
            if left > q[0]: # remove left
                q.popleft()
            
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1

        return res

