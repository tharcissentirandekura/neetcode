class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        explored = set()
        for num in nums:
            if num in explored:
                return True
            explored.add(num)
        return False

         