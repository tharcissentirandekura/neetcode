class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        - Order the strings first
        - convert them to set
        - ifi both are zero or if s == t return true
        """

        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False
        