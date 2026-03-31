class Solution:
    def validPalindrome(self, s: str) -> bool:
        # for a palendrome
        # helper tpo check if a substring is a palendrome: string without one character
        def is_palendrome(i,j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1

        while left <= right:
            # if we get a mismatch, we skip and then check if this is a palendrome
            if s[left] != s[right]:
                # mismatch
                # skipt left character: so left = left+ 1
                # skip right - 1 character: so right = right - 1
                return ( is_palendrome(left + 1,right) or
                     is_palendrome(left,right - 1))
            left += 1
            right -= 1

        return True
