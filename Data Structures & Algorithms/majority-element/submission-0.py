class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}

        for val in nums:
            maps[val] = 1 + maps.get(val,0)
        majority = float("-inf")
        value = 0
        for val,count in maps.items():
            if count > len(nums) // 2 and count > majority:
                majority = count
                value = val
        print(maps)
        return value
            