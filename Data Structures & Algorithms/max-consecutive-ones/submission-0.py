class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        localCount = 0
        for num in nums:
            if num == 1:
                localCount+= 1
            else:
                localCount = 0
            maxOnes = max(localCount,maxOnes)
            # print(num,localCount,maxOnes)
        return maxOnes

