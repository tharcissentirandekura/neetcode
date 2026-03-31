class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # variable sliding window: no size specified

        # have L,R =0,0
        # move R until we have a duplicates
        # if so: condition is broken: shrink L
        # if condition valid again: expand R


        left,right = 0,0

        res = 0
        sequence = set()
        while right < len(s):
            while s[right] in sequence:
                sequence.remove(s[left])
                left += 1
            else:
                sequence.add(s[right])
                right += 1
            
            res = max(res,right - left)
        print("The res:",res)
        return res
            
        