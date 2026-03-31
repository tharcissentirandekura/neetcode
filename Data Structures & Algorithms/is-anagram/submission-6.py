class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_count = [0] * 26 # O(26)
        t_count = [0] * 26 # O(26)
       
        for i in range(len(s)): # O(n)
            s_index = ord(s[i]) - ord('a') 
            t_index = ord(t[i]) - ord('a')
            s_count[s_index] += 1
            t_count[t_index] += 1
        print(s_count,":",t_count)
        return s_count == t_count


    

        