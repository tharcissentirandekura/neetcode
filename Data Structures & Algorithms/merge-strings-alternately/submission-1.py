class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # O(n) space and O(n) time
        res = []

        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        # add the rest
        # I use word1[i + 1: ] or word2[i+1:] because one may be empty and it doesn't make a change
        res.append(word1[i + 1: ] or word2[i+1:])

        return "".join(res)