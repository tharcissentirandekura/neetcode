class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # I kinda solved this problem from google DSA series
        # if the last value is not len(nums)
        #  that means it is missing
        # otherwise, we scan from left to right and check from if next value is 1+ current
        # ignore duplicaes
        # 0 is neigher pos or negative
        unique = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in unique:
                return i
        return len(nums) + 1
