class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')

        i,j = 0,0
        curr_sum = 0
        while j < len(nums):
            # we expand as long as the sum < target
            curr_sum += nums[j]
            while curr_sum >= target:
                curr_sum -= nums[i]
                minLength = min(minLength,(j - i + 1))
                i += 1
            j += 1
        return minLength if minLength != float('inf') else 0
