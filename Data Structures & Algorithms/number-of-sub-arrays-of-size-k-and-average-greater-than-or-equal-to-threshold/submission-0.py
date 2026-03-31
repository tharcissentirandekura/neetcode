class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        i,j = 0,0
        total = 0
        curr_sum = 0

        while j < len(arr):
            curr_sum += arr[j]
            if j - i + 1 == k:
                # check 
                if curr_sum / k >= threshold:
                    total += 1
                # remove elements from left
                curr_sum -= arr[i]
                i += 1
            j += 1

        return total
