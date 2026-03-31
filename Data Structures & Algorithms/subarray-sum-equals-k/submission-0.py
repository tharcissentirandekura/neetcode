class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum since it has negatives
        # otherwise, we would use sliding window

        prefix_sum = 0 #running sum
        count = 0 

        seen = {0:1} #index 0 is seen

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in seen:
                # we got this computation, increment count by how many this is seen
                count += seen[prefix_sum - k]
            # update prefix sum or add it if not encounterd
            seen[prefix_sum] = seen.get(prefix_sum,0) + 1
        return count
        

