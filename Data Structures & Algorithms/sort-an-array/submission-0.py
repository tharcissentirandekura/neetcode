class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 
        # return sorted(nums)
        # Input: nums (integers)
        # Output: nums sorted in ascending order

        # split it into two halves
        # merge twose two subarrays

        def mergeSort(nums): #recursion
            # to do everything
            #
            # base case
            if len(nums) <= 1:
                return nums
            # slicing
            part1 = mergeSort(nums[:len(nums) // 2])
            part2 = mergeSort(nums[len(nums) // 2:])

            return merge(part1,part2)
            
        def merge(part1,part2):
            # case
            # if one is empty: we can return the other one
            # both are empty: won't happen here
            res = []
            # if both lists have numbers
            # part1 = [10] part2 = [9]

            l1, l2 = 0, 0

            while  l1 < len(part1) and l2 < len(part2):
                if part1[l1] < part2[l2]:
                    res.append(part1[l1])
                    # move l1
                    l1 += 1
                else:
                    res.append(part2[l2])
                    l2 += 1
            # which l1 is still less htat the part corresponding to it
    
            res.extend(part1[l1:])
            res.extend(part2[l2:])
           
            return res
        return mergeSort(nums)

        



















        