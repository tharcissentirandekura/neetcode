class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uppercase
        # choose up tp k hcaracters of the s and repace them with any other 
        # upper English character

        # to make alll characters in string unique: replace the characteers with 
        # frequency more that one
        # replace with the most frequent char as it minimizes the # of replacement


        # get the most frequent char
        max_count = 0
        res = 0
        left = right = 0
        window = {}

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char,0)

            max_count = max(max_count,window[char])
                
            if (right - left + 1) - max_count > k:
                window[s[left]] -= 1
                left += 1
                
        return max(res,right - left+1)


