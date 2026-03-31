class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                # num is the start
                current = num
                length = 1 #now we found one
                while current + 1 in numSet: #if the next
                    current += 1
                    length +=1
                longest = max(length,longest)
        return longest 
            
                     


        