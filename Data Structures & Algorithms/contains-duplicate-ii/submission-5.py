class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,j = 0,0
        window = set()
        
        while j < len(nums):
            if nums[j] in window:
                return True
            window.add(nums[j])

            if j - i + 1 > k:
                window.remove(nums[i])
                i += 1
            j += 1
        return False
                
            


