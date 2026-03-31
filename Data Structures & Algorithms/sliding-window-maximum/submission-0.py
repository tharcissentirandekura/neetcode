class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use a deque for optimization
        # queue will hold the values in the window
        # every time we want to add one we add to queue adn remove to it

        q = deque()

        # this is a fixed window
        window = nums[:k]

        slide_max = max(nums)
        res = []
        
        for i in range(len(nums) - k):
            res.append(max(window))
            print(window)
            # remove one and add one
            window = nums[i + 1: i + k + 1]
        res.append(max(nums[len(nums) - k: len(nums)]))
        return res