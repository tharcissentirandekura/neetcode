class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        1.
        - Order the strings first by alphabetical order
        - check if those orderd strings are equal
        2.
        - check if s and t have same length and if so :
        - loop through s and check if each character is in t:
        if so:
            return True
        otherwise :
        return False
        """

        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False
        # if len(s) == len(t):
        #     for char in s:
        #         if char not in t:
        #             return False
        #     return True
        # else:
        #     return False



        