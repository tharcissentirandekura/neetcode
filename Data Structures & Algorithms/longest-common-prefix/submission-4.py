class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # same

        # we can find the small string
        # apply a window check

        small_s = ""
        minimum = float('inf')

        for string in strs:
            if len(string) < minimum:
                small_s = string
                minimum = len(string)

        k = 0
        for i in range(len(small_s)):
            for word in strs:
                if word[i] != small_s[i]:
                    return small_s[:i]
                    break
        return small_s









                