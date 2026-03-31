class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # min window
        # substring of s : where every characters of t are present


        # start with window of size len(t)
        # use some counter to check if all characters are there

        window_count = {}
        t_count = {}

        # t count
        for char in t:
            t_count[char] = 1 + t_count.get(char,0)
        

        left,right = 0,0

        have,needed = 0, len(t_count) # needed match to be valid

        res = ""
        min_len = float('inf')

        while right < len(s):
            # expand
            char = s[right]
            window_count[char] = 1 + window_count.get(char,0)

            if char in t and window_count[char] == t_count[char]:
                have += 1
            
            # shrink window while it is valid
            while have == needed:
                if min_len > (right - left + 1):
                    min_len = (right - left + 1)
                    res = s[left:right + 1]
                # shrink
                window_count[s[left]] -= 1

                if s[left] in t_count and  window_count[s[left]] < t_count[s[left]]:
                        have -= 1
                left += 1
            right += 1

        return res
        

        




