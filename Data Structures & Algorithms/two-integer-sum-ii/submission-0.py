class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index 1 < index 2
        # index1 + index 2 = target
        # can't use any other new data structure like set or map
        # since it is sorted we can use a binary search kind of technique

        """ 
            calculate sum of first and second
            curr_sum = nums[left] + nums[right]

            is the target > curr_sum, we need to move forward because left value can't 
            get us anywhere
            if target < curr_sum, so we need to decrement right pointer 1 at a time

        
        """

        l,r = 0,len(numbers) - 1
        while l <= r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l + 1, r + 1]
            elif curr < target: 
                l += 1
            else:
                r -= 1
            





        