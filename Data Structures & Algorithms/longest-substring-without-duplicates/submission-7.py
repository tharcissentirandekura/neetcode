class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use some count of distinct so far
        # if we see the duplicate
        # we update our start to be at this character that broke the substring sequence
        # QUESTION: CAN WE DO WE IN NO EXTRA SPACE? 
        substring = set()
        
        left = 0
        right = 0
        count = 0
        longest = 0

        while right < len(s):
            while s[right] in substring:
                substring.remove(s[left])
                # move on
                left += 1
                count -= 1
            # check if this was the max window
            count += 1
            longest = max(longest, count)
            # expand the window
            substring.add(s[right])
            right += 1
            
        return longest