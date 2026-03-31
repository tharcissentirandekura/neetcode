class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # avoid duplicates
        numSet = set()
        for num in nums:
            numSet.add(num)
        # dp probem
        memo = [1] * len(nums) #because choosing one number is possible
        # now go through the first round and fill in memo 
        current = 0
        while current < len(nums):
            nextNum = nums[current] + 1
            if nextNum in numSet:
                print(f"The next of {nums[current]} is :{nextNum}")
                nums[current] = nextNum
                memo[current] += 1
            else:
                current += 1
                if current < len(nums):
                    print(f"The current number is {current}: {nums[current]}")
        
        
        return max(memo)


        