class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #same values
                continue
            l,r = i + 1,len(nums) - 1

            while l < r:
                triplets = a + nums[l] + nums[r]
                if triplets > 0: # decrease the sum
                    r -= 1
                elif triplets < 0:
                    # increment sum
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[ l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
