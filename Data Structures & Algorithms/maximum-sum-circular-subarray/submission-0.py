class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax,globalMin = nums[0],nums[0]
        curMax = curMin = 0
        total_sum = 0
        for curNum in nums:
            curMax = max(curNum,curMax + curNum)
            curMin = min(curNum, curMin + curNum )

            # increat total cum
            total_sum += curNum
            # gloabl max and min
            globalMax = max(globalMax,curMax)
            globalMin = min(globalMin,curMin)
        return max(globalMax,total_sum - globalMin) if globalMax > 0 else globalMax