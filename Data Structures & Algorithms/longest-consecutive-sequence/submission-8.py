class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numSet = set(nums)
        for i in range(len(nums)):
            
            if nums[i] - 1 not in nums:
                curr_max = 1    
                curr = nums[i]
                while curr + 1 in nums:
                    curr += 1
                    curr_max += 1
                longest = max(longest,curr_max)
                curr_max = 0
        return longest

