class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        - use a hashmap to store visited numbers
        - loop thorugh the list
        - see the number you need to add to the current exist
        in the hashmap ( target - current)
        - if so, return those two indexes
        - otherwise, return Nothing
        """

        visited = {}

        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in visited:
                return [visited[desired],i]
            else:
                visited[nums[i]] = i

        