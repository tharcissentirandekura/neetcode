class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find duplicates
        # use two pointers
        # fast and slow
        # use Tortoise and Hare 
        # fast points start with the slow value as index

        # find intersection
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        # find entrance to cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


        