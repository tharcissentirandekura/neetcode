class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,currSet = [],[]

        def generateSet(i,nums,currSet:List,res:List):
            if i == len(nums):
                res.append(currSet.copy())
                return 
            # include current number
            currSet.append(nums[i])
            generateSet(i + 1, nums,currSet,res)
            currSet.pop()

            # SKip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # Exclude current 
            generateSet(i + 1,nums,currSet,res)
            
        nums.sort()
        generateSet(0,nums,currSet,res)
        return res
