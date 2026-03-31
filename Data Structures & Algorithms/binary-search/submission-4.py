class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        index = 0

        center = len(nums) // 2
        left = nums[:center]
        right = nums[center + 1:]
        current = nums[center]

        if target == current:
            return center
        
        elif target > current:
            result = self.search(right,target)
            if result != -1:
                return center + 1 + result
            else:
                return - 1
        else:
            return self.search(left,target)
        
