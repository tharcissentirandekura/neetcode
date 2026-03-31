class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                # nums2 is bigger
                nums1[k] = nums2[j]
                j -= 1
            else:
                # move the value in nums1 front to the end at k
                nums1[k] = nums1[i]
                i -= 1
            # reduce k each iteration
            k -= 1

        # add reamining 
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



        