class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each step, we can take the value 
        #  or not
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            # if it goes to negative, reset it to 0
            print(currSum,":", maxSum)
            currSum = max(currSum,0)
            currSum += num
            maxSum = max(currSum,maxSum)
        return maxSum

            