class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0

        zero_count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            # shrink the window
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            # check the max
            max_count = max(max_count , i - l + 1)
            # expand 
        return max_count