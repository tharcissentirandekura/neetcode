class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s) - 1):
            old_s = s[i]
            new_s = s[i + 1]
            print(ord(new_s),ord(old_s))
            score = abs(ord(new_s) - ord(old_s))
            total +=score
        return total